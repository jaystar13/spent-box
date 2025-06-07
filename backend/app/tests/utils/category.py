from sqlmodel import Session

from app import crud
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string
from app.schemas import CategoryWithKeywordsCreate


def create_random_category_with_keywords(db: Session):
    user = create_random_user(db)
    owner_id = user.id
    assert owner_id is not None
    category_in = CategoryWithKeywordsCreate(
        name="식비", color="#FF5733", keywords=["편의점", "커피숍", "배달의민족"]
    )
    return crud.create_category_with_keywords(
        session=db, current_user=user, data=category_in
    )
