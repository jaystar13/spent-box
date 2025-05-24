from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
    user_data = {"name": "Alice", "email": "alice@example.com"}
    response = client.post("/api/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert "id" in data
