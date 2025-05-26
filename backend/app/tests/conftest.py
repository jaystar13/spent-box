# import pytest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from app.database import Base
# from app.models.users_model import User
# from app.main import app

# # 테스트용 DB 설정
# SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# TestingSessionLocal = sessionmaker(bind=engine)

# TEST_USER_ID = 1


# @pytest.fixture(scope="module")
# def db():
#     print("테이블 생성 시작")  # 👉 디버깅용
#     Base.metadata.create_all(bind=engine)
#     print("테이블 목록:", Base.metadata.tables.keys())  # 👉 디버깅용
#     db_session = TestingSessionLocal()
#     yield db_session
#     db_session.close()
#     Base.metadata.drop_all(bind=engine)


# @pytest.fixture(scope="module")
# def client(db):
#     from fastapi import FastAPI
#     from fastapi.testclient import TestClient
#     from app.api.endpoints import user_api
#     from app.database import get_db

#     test_app = FastAPI()
#     test_app.include_router(user_api.router, prefix="/api/users", tags=["users"])
#     test_app.dependency_overrides[get_db] = lambda: db

#     with TestClient(app) as test_client:
#         yield test_client

#     test_app.dependency_overrides.clear()


# @pytest.fixture(scope="function")
# def test_user_id():
#     return TEST_USER_ID


from collections.abc import Generator
from fastapi.testclient import TestClient
import pytest
from sqlmodel import Session, delete

from app.core.config import settings
from app.core.db import engine, init_db
from app.main import app
from app.models import Item, User
from app.tests.utils.utils import get_superuser_token_headers


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        init_db(session)
        yield session
        statement = delete(Item)
        session.exec(statement)
        statement = delete(User)
        session.exec(statement)
        session.commit()


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient) -> dict[str, str]:
    return get_superuser_token_headers(client)
