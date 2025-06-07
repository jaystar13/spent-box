import uuid
from fastapi import HTTPException
from sqlmodel import Session, select
from app.models import (
    Category,
    CategoryKeyword,
    User,
)
from app.schemas import CategoryCreate


def create_category(
    *, session: Session, current_user: User, category_in: CategoryCreate
) -> Category:
    db_category = Category(
        name=category_in.name,
        color=category_in.color,
        user_id=current_user.id,
    )
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category


def get_category_with_keywords(*, session: Session, category_id: uuid.UUID):
    statement = select(Category).where(Category.id == category_id)
    result = session.exec(statement)
    category = result.first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    _ = category.keywords

    return category


def get_category_by_keyword(*, session: Session, keyword: str) -> Category | None:
    statement = (
        select(Category)
        .join(CategoryKeyword)
        .where(CategoryKeyword.keyword.contains(keyword))
        .limit(1)
    )
    category = session.exec(statement).first()
    return category
