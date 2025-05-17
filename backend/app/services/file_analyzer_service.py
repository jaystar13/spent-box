from datetime import datetime
from typing import Any
from fastapi import UploadFile

from app.repositories.category_repository import get_user_categories
from app.schemas.file_analyzer_schemas import FileAnalyzeRequest
from app.services.categorization_service import ExpenseCategorizationService
from app.services.converter.converter_factory import get_converter


async def analyze_uploaded_file(file: UploadFile, request: FileAnalyzeRequest) -> Any:

    converter = get_converter(request.institution)

    if not converter.is_supported_file(file):
        raise ValueError(f"{request.institution} 은 이 파일 형식을 지원하지 않습니다.")

    converted_data = await converter.transform(file)

    now = datetime.now()
    year = request.year or now.year
    month = request.month or now.month

    # 사용자별 카테고리 로딩
    user_categories = await get_user_categories(request.user_id)

    categorizer = ExpenseCategorizationService(category_data=user_categories)
    categorized = categorizer.categorize(converted_data, year=year, month=month)

    return {
        "user_id": request.user_id,
        "institution": request.institution,
        "count": len(converted_data),
        "categorized": categorized,
    }
