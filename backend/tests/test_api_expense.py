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
    # data = response.json()

    # assert "message" in data
    # assert data["message"] == "월별 지출이 성공적으로 저장되었습니다."
