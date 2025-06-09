from io import BytesIO
from fastapi import UploadFile
import pandas as pd
from app.crud.file_upload.converter.base import UploadFileBaseConverter


class KbCardConverter(UploadFileBaseConverter):
    def is_supported_file(self, file: UploadFile):
        return super().is_supported_file(file)

    async def parse_raw(self, file: UploadFile) -> pd.DataFrame:
        contents = await file.read()
        df = pd.read_excel(BytesIO(contents), sheet_name=0, header=1)

        # 잘못된 행 제거
        df = df[df["이용일자"] != "이용일자"]
        df = df[df["이용하신 가맹점"].notna()]
        df = df[~df["이용하신 가맹점"].astype(str).str.contains("소계")]
        df = df[df["이용일자"].notna() & (df["이용일자"].astype(str).str.strip() != "")]

        # 필요한 컬럼 추출 및 이름 변경
        df = df[["이용일자", "이용카드", "이용하신 가맹점", "이용금액"]].copy()
        df.columns = ["date", "card_type", "merchant", "amount"]

        # 카드명 치환
        card_map = {
            "마스터058": "KB카드-가족",
            "마스터834": "KB카드-본인",
        }

        df["card_type"] = df["card_type"].map(card_map).fillna(df["card_type"])

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
            parts = date_str.strip().split(".")
            if len(parts) == 3:
                year = int(parts[0])
                year += 2000 if year < 100 else 0
                return f"{year:04d}-{int(parts[1]):02d}-{int(parts[2]):02d}"
            return date_str
        except Exception:
            return date_str
