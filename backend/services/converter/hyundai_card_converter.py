from io import BytesIO
import pandas as pd
from fastapi import UploadFile, HTTPException
from backend.services.converter.base_converter import BaseConverter


class HyundaiCardConverter(BaseConverter):

    def is_supported_file(self, file: UploadFile):
        return file.filename.endswith((".xls", ".xlsx"))

    async def parse_raw(self, file: UploadFile) -> pd.DataFrame:
        contents = await file.read()

        try:
            # 전체 데이터를 일단 다 읽고
            preview_df = pd.read_excel(
                BytesIO(contents), sheet_name=0, header=None, engine="openpyxl"
            )
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="암호가 설정된 엑셀 파일은 업로드할 수 없습니다. 비밀번호를 제거한 후 다시 시도해주세요.",
            )

        # 헤더 행 찾기: '이용일', '가맹점명', '이용금액'이 모두 포함된 첫 번째 행
        header_row_idx = None
        for idx, row in preview_df.iterrows():
            row_values = row.astype(str).tolist()
            if all(col in row_values for col in ["이용일", "가맹점명", "이용금액"]):
                header_row_idx = idx
                break

        if header_row_idx is None:
            raise HTTPException(
                status_code=400,
                detail="엑셀에 '이용일', '가맹점명', '이용금액' 컬럼이 포함된 헤더 행을 찾을 수 없습니다.",
            )

        # 해당 인덱스를 헤더로 다시 읽음
        df = pd.read_excel(
            BytesIO(contents), sheet_name=0, header=header_row_idx, engine="openpyxl"
        )

        # 필요한 컬럼 추출 및 이름 변경
        df = df[["이용일", "가맹점명", "이용금액"]].copy()
        df.insert(1, "이용카드", "현대카드")
        df.columns = ["date", "card_type", "merchant", "amount"]

        return df

    def normalize(self, df: pd.DataFrame) -> pd.DataFrame:
        df["amount"] = df["amount"].apply(self._normalize_amount)
        df["date"] = df["date"].apply(self._normalize_date)
        return df

    def _normalize_amount(self, amount_str):
        try:
            return int(str(amount_str).replace(",", "").replace("원", "").strip())
        except Exception:
            return 0

    def _normalize_date(self, date_str):
        try:
            parts = str(date_str).strip().split(".")
            if len(parts) == 3:
                year = int(parts[0])
                year += 2000 if year < 100 else 0
                return f"{year:04d}-{int(parts[1]):02d}-{int(parts[2]):02d}"
            return date_str
        except Exception:
            return date_str
