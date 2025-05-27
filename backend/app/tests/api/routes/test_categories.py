from typing import Any

from fastapi.testclient import TestClient

from app.core.config import settings


def test_create_category(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    data = {"name": "식비", "color": "#FFCC00"}
    response = client.post(
        f"{settings.API_V1_STR}/categories/",
        headers=superuser_token_headers,
        json=data,
    )

    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["color"] == data["name"]
    assert "id" in content
    assert "created_at" in content
