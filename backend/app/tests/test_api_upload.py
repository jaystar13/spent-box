import os
from fastapi.testclient import TestClient
from app.deps.auth import get_current_user_id
from app.main import app

client = TestClient(app)


def override_get_current_user_id():
    return 1


app.dependency_overrides[get_current_user_id] = override_get_current_user_id


def test_analyze_uploaded_file_api():
    # 테스트용 샘플 HTML 파일 경로
    base_dir = os.path.dirname(__file__)  # 현재 test 파일 기준
    sample_file_path = os.path.join(base_dir, "resources", "kb_sample.xlsx")

    with open(sample_file_path, "rb") as f:
        response = client.post(
            "/api/upload/analyze",
            files={
                "file": (
                    "kb_sample.xlsx",
                    f,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
            },
            data={"institution": "kb-card", "year": "2025", "month": "2"},
        )

    print(response.status_code)
    print(response.text)

    assert response.status_code == 200  # 또는 기대되는 코드로 수정
    assert "result" in response.json() or isinstance(response.json(), dict)
