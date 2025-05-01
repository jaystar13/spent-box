from io import BytesIO
from fastapi import UploadFile
from backend.services.converter.base_converter import BaseConverter
import pandas as pd


class KbCardConverter(BaseConverter):

    def is_supported_file(self, file: UploadFile):
        return file.filename.endswith((".xls", ".xlsx"))

    async def transform(self, file: UploadFile):
        df = await self.parse_raw(file)
        normalized = self.normalize(df)
        return normalized.to_dict(orient="records")

    async def parse_raw(self, file: UploadFile) -> pd.DataFrame:
        contents = await file.read()
        return pd.read_excel(BytesIO(contents))

    def normalize(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df[["날짜", "금액", "사용처"]].rename(
            columns={"날짜": "date", "금액": "amount", "사용처": "description"}
        )
        df["amount"] = df["amount"].astype(int)
        return df
