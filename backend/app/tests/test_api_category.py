import uuid


def test_create_category(client):
    user_id = uuid.uuid4()  # 임의 사용자 ID

    # 인증 의존성 오버라이드
    from app.deps.auth import get_current_user_id

    def override_get_current_user_id():
        class DummyUser:
            id = user_id

        return DummyUser()

    client.app.dependency_overrides[get_current_user_id] = override_get_current_user_id

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
