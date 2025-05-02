from fastapi import UploadFile
from backend.services.converter.base_converter import BaseConverter
import pandas as pd
from bs4 import BeautifulSoup


class KbCardConverter(BaseConverter):

    def is_supported_file(self, file: UploadFile):
        return file.filename.endswith((".html", ".htm"))

    async def transform(self, file: UploadFile):
        df = await self.parse_raw(file)
        normalized = self.normalize(df)
        return normalized.to_dict(orient="records")

    async def parse_raw(self, file: UploadFile) -> pd.DataFrame:
        contents = await file.read()
        soup = BeautifulSoup(contents, "html.parser")

        table = soup.find("table", id="usage1")
        tbody = table.find("tbody", id="list_pe01")
        rows = tbody.find_all("tr")

        data = []

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 6:
                continue  # 필요한 데이터가 부족하면 건너뜀

            card_name = cols[1].get_text(strip=True)  # 이용카드

            if card_name or card_name.strip() != "":
                data.append(
                    {
                        "date": cols[0].get_text(strip=True),
                        "cardName": card_name,
                        "merchant": cols[3].get_text(strip=True),
                        "amount": cols[5].get_text(strip=True),
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
