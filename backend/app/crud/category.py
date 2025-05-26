from sqlmodel import Session
from app.models import Category, CategoryCreate, CategoryKeyword, CategoryKeywordCreate


def create_category(*, session: Session, category_in: CategoryCreate) -> Category:
    db_category = Category.model_validate(category_in)
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
