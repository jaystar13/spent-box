from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DB_URL = "sqlite:///:memory:"

engine = create_engine(DB_URL, pool_size=50, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    print("database get_db 실행")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
