from io import BytesIO
import pandas as pd
from fastapi import UploadFile
from app.services.converter.base_converter import BaseConverter


class HanaCardConverter(BaseConverter):

    def is_supported_file(self, file: UploadFile):
        return file.filename.endswith((".html", ".htm"))

    async def parse_raw(self, file: UploadFile) -> pd.DataFrame:
        contents = await file.read()
        df = pd.read_excel(BytesIO(contents), sheet_name=0)
        df.columns = df.columns.str.strip

        if not {"승인일자", "가맹점명", "승인금액"}.issubset(df.columns):
            raise ValueError(
                "필수 컬럼(승인일자, 가맹점명, 승인금액)이 누락되었습니다."
            )

        df = df[["승인일자", "가맹점명", "승인금액"]]
        df = df.rename(
            columns={"승인일자": "date", "가맹점명": "merchant", "승인금액": "amount"}
        )

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
