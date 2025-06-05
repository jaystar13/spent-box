from sqlmodel import Session
from app.models import (
    Category,
    CategoryKeyword,
    User,
)
from app.schemas import (
    CategoryWithKeywordsCreate,
    CategoryKeywordCreate,
)


def create_category_keyword(
    *, session: Session, keyword_in: CategoryKeywordCreate
) -> CategoryKeyword:
    db_keyword = CategoryKeyword(
        category_id=keyword_in.category_id, keyword=keyword_in.keyword
    )
    session.add(db_keyword)
    session.commit()
    session.refresh(db_keyword)
    return db_keyword


def create_category_with_keywords(
    *,
    session: Session,
    current_user: User,
    data: CategoryWithKeywordsCreate,
) -> Category:
    category = Category(name=data.name, color=data.color, user_id=current_user.id)
    session.add(category)
    session.flush()

    for kw in data.keywords:
        keyword = CategoryKeyword(category_id=category.id, keyword=kw)
        session.add(keyword)

    session.commit()
    session.refresh(category)
    return category
