from bs4 import BeautifulSoup
import pandas as pd
from fastapi import UploadFile
from backend.services.converter.base_converter import BaseConverter


class HanaCardConverter(BaseConverter):

    def is_supported_file(self, file: UploadFile):
        return file.filename.endswith((".html", ".htm"))

    async def transform(self, file: UploadFile):
        df = await self.parse_raw(file)
        normalized = self.normalize(df)
        return normalized.to_dict(orient="records")

    async def parse_raw(self, file: UploadFile) -> pd.DataFrame:
        contents = await file.read()
        soup = BeautifulSoup(contents, "html.parser")

        rows = soup.find_all("tr")  # 모든 행 찾기

        data = []

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 3:
                continue  # 필요한 데이터가 부족하면 건너뜀

            usage_date = cols[0].get_text(strip=True)  # 이용일자
            merchant = cols[1].get_text(strip=True)  # 이용가맹점(은행)
            amount = cols[2].get_text(strip=True)  # 이용금액

            if "/" in usage_date and amount.replace(",", "").isdigit():
                data.append(
                    {
                        "date": cols[0].get_text(strip=True),
                        "cardName": "하나카드",
                        "merchant": merchant,
                        "amount": amount,
                    }
                )

        return pd.DataFrame(data)

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
