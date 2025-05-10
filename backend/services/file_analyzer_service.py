from typing import Any
from fastapi import UploadFile

from backend.services.converter.converter_factory import get_converter


async def analyze_uploaded_file(
    file: UploadFile, institution: str, user_id: int
) -> Any:

    converter = await get_converter(institution)

    if not converter.is_supported_file(file):
        raise ValueError(f"{institution} 은 이 파일 형식을 지원하지 않습니다.")

    converted_data = await converter.transform(file)

    return {
        "user_id": user_id,
        "institution": institution,
        "count": len(converted_data),
        "data": converted_data,
    }
