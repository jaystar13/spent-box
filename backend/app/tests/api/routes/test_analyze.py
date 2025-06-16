import io
import os
from fastapi import UploadFile
from fastapi.testclient import TestClient
import pytest
from app.core.config import settings
from app.api.routes import analyze


@pytest.fixture
def fake_excel_file():
    # 가짜 Excel 파일 생성 (.xlsx 확장자, 실제 내용은 중요하지 않음)
    return (
        "test.xlsx",
        io.BytesIO(b"Fake Excel Content"),
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


def test_analyze_upload(
    client: TestClient,
    superuser_token_headers: dict[str, str],
    monkeypatch,
    fake_excel_file,
):
    def mock_validate_file(file):
        return True

    def mock_analyze_file(current_user, year, month, payment_method, file):
        return {"total": 500000, "categories": {"식비": 50000, "교통": 10000}}

    monkeypatch.setattr(analyze, "validate_file", mock_validate_file)
    monkeypatch.setattr(analyze, "analyze_file", mock_analyze_file)

    response = client.post(
        f"{settings.API_V1_STR}/analyze-upload/",
        data={
            "year": 2025,
            "month": 6,
            "payment_method": "KB국민카드",
        },
        headers=superuser_token_headers,
        files={"file": fake_excel_file},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["institution"] == "KB국민카드"
    assert "summary" in data
