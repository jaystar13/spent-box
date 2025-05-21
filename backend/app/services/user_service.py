from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.models.users_model import User


def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, new_data: UserCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = new_data.name
        user.email = new_data.email
        db.commit()
        db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
