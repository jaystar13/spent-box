import io
from fastapi import UploadFile
import pandas as pd


def validate_file(file: UploadFile) -> bool:
    filename = file.filename.lower()
    return filename.endswith(".xlsx") or filename.endswith(".xls")


async def analyze_file(file: UploadFile, institution: str) -> dict:
    contents = await file.read()

    try:
        df = pd.read_excel(io.BytesIO(contents))
    except Exception:
        return {"error": "엑셀 파일만 지원합니다."}

    dummy_result = {
        "total_spending": 123456,
        "color": "#F000000",
        "categories": {"식비": 45000, "쇼핑": 30000, "교통": 20000},
    }

    return dummy_result
