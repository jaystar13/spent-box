import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models.users_model import User
from app.main import app

# 테스트용 DB 설정
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(bind=engine)

TEST_USER_ID = 1


@pytest.fixture(scope="session")
def db():
    print("테이블 생성 시작")  # 👉 디버깅용
    Base.metadata.create_all(bind=engine)
    print("테이블 목록:", Base.metadata.tables.keys())  # 👉 디버깅용
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session")
def client(db):
    from fastapi.testclient import TestClient
    from app.database import get_db

    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
def test_user_id():
    return TEST_USER_ID
