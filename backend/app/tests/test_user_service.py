import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.schemas.user_schema import UserCreate
from app.services.user_service import create_user, delete_user, get_user, update_user


# 테스트용 DB
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_create_user(db):
    user = UserCreate(name="Alice", email="alice@example.com")
    result = create_user(db, user)
    assert result.name == "Alice"
    assert result.email == "alice@example.com"


def test_get_user(db):
    user = create_user(db, UserCreate(name="Bob", email="bob@example.com"))
    fetched = get_user(db, user.id)
    assert fetched.id == user.id


def test_update_user(db):
    user = create_user(db, UserCreate(name="Charlie", email="c@example.com"))
    updated = update_user(
        db, user.id, UserCreate(name="Chuck", email="chuck@example.com")
    )
    assert updated.name == "Chuck"


def test_delete_user(db):
    user = create_user(db, UserCreate(name="Dave", email="d@example.com"))
    deleted = delete_user(db, user.id)
    assert deleted.id == user.id
    assert get_user(db, user.id) is None
