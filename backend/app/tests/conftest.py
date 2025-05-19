import uuid
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app.deps.auth import get_current_user_id

TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

TEST_USER_ID = uuid.UUID("11111111-1111-1111-1111-111111111111")


# ✅ 세션 전체에서 한 번만 실행해서 테이블 생성
@pytest.fixture(scope="session", autouse=True)
def create_test_tables():
    print("create_test_tables1111")
    Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user_id():
    class DummyUser:
        id = TEST_USER_ID

    return DummyUser()


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user_id] = override_get_current_user_id


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def test_user_id():
    return TEST_USER_ID
