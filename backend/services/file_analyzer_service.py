from typing import Any
from fastapi import UploadFile

from backend.services.converter.converter_factory import get_converter


async def analyze_uploaded_file(
    user_id: int, file: UploadFile, institution: str
) -> Any:
    converter = get_converter(institution)

    if not converter.is_supported_file(file):
        raise ValueError(f"{institution} 은 이 파일 형식을 지원하지 않습니다.")

    converted_data = converter.transform(file)

    return {
        "user_id": user_id,
        "institution": institution,
        "count": len(converted_data),
        "data": converted_data,
    }
