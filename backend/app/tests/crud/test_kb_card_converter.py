import io
import json
import os
from fastapi import UploadFile
import pytest

from app import crud


@pytest.mark.asyncio
async def test_kb_card_converter_transform():
    # 테스트용 샘플 HTML 파일 경로
    root_path = os.getcwd()
    sample_file_path = os.path.join(
        root_path, "app", "tests", "resources", "kb_sample.xlsx"
    )

    # 파일이 존재하는지 확인
    assert os.path.exists(
        sample_file_path
    ), f"테스트 파일이 존재하지 않습니다: {sample_file_path}"

    # UploadFile 객체로 래핑
    with open(sample_file_path, "rb") as f:
        file_data = f.read()
        upload_file = UploadFile(filename="kb_sample.xlsx", file=io.BytesIO(file_data))

    converter = crud.KbCardConverter()
    result = await converter.transform(upload_file)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    # 결과 확인
    assert isinstance(result, list)
    assert len(result) > 0
    assert all(
        "date" in item and "merchant" in item and "amount" in item for item in result
    )
