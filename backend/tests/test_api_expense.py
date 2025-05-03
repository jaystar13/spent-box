from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_post_monthly_expense():
    payload = {
        "year": 2025,
        "month": 4,
        "expenses": [
            {"category": "식비", "amount": 300000},
            {"category": "교통비", "amount": 120000},
        ],
    }

    response = client.post("/api/expenses/monthly", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "message" in data
    assert data["message"] == "저장 완료"

    # 데이터 구조 검증
    assert "data" in data
    result = data["data"]

    assert result["year"] == 2025
    assert result["month"] == 4
    assert isinstance(result["expenses"], list)
    assert len(result["expenses"]) == 2
    assert result["expenses"][0]["category"] == "식비"
    assert result["expenses"][0]["amount"] == 300000
