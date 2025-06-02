from sqlmodel import Session
from app.models import (
    Category,
    CategoryCreate,
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
