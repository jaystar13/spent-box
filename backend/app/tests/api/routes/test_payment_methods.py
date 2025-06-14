from fastapi.testclient import TestClient
from sqlmodel import Session

from app.core.config import settings
from app.tests.utils.payment_method import create_random_payment_method


def test_payment_method(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    data = {"name": "KB카드", "type": "신용카드", "billing_day": "15"}
    response = client.post(
        f"{settings.API_V1_STR}/payment-methods/",
        headers=superuser_token_headers,
        json=data,
    )

    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["type"] == data["type"]
    assert "id" in content
    assert "created_at" in content


def test_read_payment_method(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
):
    payment_method = create_random_payment_method(db)
    response = client.get(
        f"{settings.API_V1_STR}/payment-methods/{payment_method.id}",
        headers=superuser_token_headers,
    )

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == str(payment_method.id)
    assert data["name"] == str(payment_method.name)
    assert data["type"] == str(payment_method.type)


def test_update_payment_method(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
):
    payment_method = create_random_payment_method(db)
    update_data = {"name": "KB카드-New", "type": "신용카드-New", "billing_day": "25"}
    response = client.put(
        f"{settings.API_V1_STR}/payment-methods/{payment_method.id}",
        headers=superuser_token_headers,
        json=update_data,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["type"] == update_data["type"]


def test_delete_payment_method(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
):
    payment_method = create_random_payment_method(db)
    response = client.delete(
        f"{settings.API_V1_STR}/payment-methods/{payment_method.id}",
        headers=superuser_token_headers,
    )

    assert response.status_code == 200
    assert response.json()["ok"] is True

    get_res = client.get(
        f"{settings.API_V1_STR}/payment-methods/{payment_method.id}",
        headers=superuser_token_headers,
    )
    assert get_res.status_code == 404
