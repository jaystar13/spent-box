import io
from fastapi import UploadFile
import pandas as pd

from app.crud.file_upload.converter.factory import get_converter
from app.models.user import User


def validate_file(file: UploadFile) -> bool:
    filename = file.filename.lower()
    return filename.endswith(".xlsx") or filename.endswith(".xls")


async def analyze_file(
    *, current_user: User, year: int, month: int, institution: str, file: UploadFile
) -> dict:
    converter = get_converter(institution)

    if not converter.is_supported_file(file):
        raise ValueError(f"{institution} 은 이 파일 형식을 지원하지 않습니다.")

    converted_data = await converter.transform(file)

    now = datetime.now()
    year = year or now.year
    month = month or now.month

    # 사용자별 카테고리 로딩
    # user_categories = await get_user_categories(current_user.id)

    # categorizer = ExpenseCategorizationService(category_data=user_categories)
    # categorized = categorizer.categorize(converted_data, year=year, month=month)

    return {
        # "user_id": request.user_id,
        # "institution": request.institution,
        # "count": len(converted_data),
        # "categorized": categorized,
    }
