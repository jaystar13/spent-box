from datetime import datetime
import io
from fastapi import UploadFile
import pandas as pd

from app import crud
from app.models.user import User
from app.api.deps import SessionDep
from app.crud.categorizer import SpentListCategorizer


def validate_file(file: UploadFile) -> bool:
    filename = file.filename.lower()
    return filename.endswith(".xlsx") or filename.endswith(".xls")


def analyze_file(
    *, current_user: User, year: int, month: int, payment_method: str, file: UploadFile
) -> dict:
    converter = crud.get_converter(payment_method)

    if not converter.is_supported_file(file):
        raise ValueError(f"{payment_method} 은 이 파일 형식을 지원하지 않습니다.")

    converted_data = converter.transform(file)

    now = datetime.now()
    year = year or now.year
    month = month or now.month

    user_categories = crud.get_user_categories(session=SessionDep, user=current_user)

    categorizer = SpentListCategorizer(user_categories)
    categorized = categorizer.categorize(converted_data, year, month)

    # 사용자별 카테고리 로딩
    # user_categories = await get_user_categories(current_user.id)

    # categorizer = ExpenseCategorizationService(category_data=user_categories)
    # categorized = categorizer.categorize(converted_data, year=year, month=month)

    return {
        "user_id": current_user.id,
        "upload_file": file,
        "payment_method": payment_method,
        "categorized": categorized,
    }
