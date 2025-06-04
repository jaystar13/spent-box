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
    assert content["color"] == data["color"]
    assert "id" in content
    assert "created_at" in content


def test_create_categor_with_keywords(
    client: TestClient, superuser_token_headers: dict[str, str]
):
    payload = {
        "name": "식비",
        "color": "#FF5733",
        "keywords": ["편의점", "커피숍", "배달의민족"],
    }

    response = client.post(
        f"{settings.API_V1_STR}/categories/with-keywords",
        headers=superuser_token_headers,
        json=payload,
    )

    assert response.status_code == 201
    data = response.json()
    print(f"Data : {data}")
    assert data["name"] == "식비"
    assert len(data["keywords"]) == 3
    assert {k["keyword"] for k in data["keywords"]} == {
        "편의점",
        "커피숍",
        "배달의민족",
    }
