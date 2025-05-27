from sqlmodel import Session
from app.models import (
    Category,
    CategoryCreate,
    CategoryKeyword,
    CategoryKeywordCreate,
    User,
)


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


def create_category_keyword(
    *, session: Session, keyword_in: CategoryKeywordCreate
) -> CategoryKeyword:
    db_keyword = CategoryKeyword.model_validate(keyword_in)
    session.add(db_keyword)
    session.commit()
    session.refresh(db_keyword)
    return db_keyword
