import io
import json
import os
from fastapi import UploadFile
import pytest

from backend.services.converter.hyundai_card_converter import HyundaiCardConverter


@pytest.mark.asyncio
async def test_hyundai_card_converter_transform():
    # 테스트용 샘플 HTML 파일 경로
    base_dir = os.path.dirname(__file__)  # 현재 test 파일 기준
    sample_file_path = os.path.join(base_dir, "resources", "hyundai_sample.xlsx")

    with open(sample_file_path, "rb") as f:
        file_data = f.read()
        upload_file = UploadFile(filename="kb_sample.xlsx", file=io.BytesIO(file_data))

    converter = HyundaiCardConverter()
    result = await converter.transform(upload_file)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    # 결과 확인
    assert isinstance(result, list)
    assert len(result) > 0
    assert all(
        "date" in item
        and "card_type" in item
        and "merchant" in item
        and "amount" in item
        for item in result
    )
