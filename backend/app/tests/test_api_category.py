import uuid


def test_create_category(client):
    # 테스트 데이터
    payload = {
        "name": "식비",
        "color": "#FF5733",
        "keywords": [
            {"keyword": "배달"},
            {"keyword": "편의점"},
        ],
    }

    response = client.post("/api/categories/", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "식비"
    assert data["color"] == "#FF5733"
    assert len(data["keywords"]) == 2
    assert {kw["keyword"] for kw in data["keywords"]} == {"배달", "편의점"}
