from sqlmodel import Session

from app import crud
from app.tests.utils.category import create_random_category_with_keywords


def test_get_category_by_keyword_found(db: Session):
    category = create_random_category_with_keywords(db)
    result = crud.get_category_by_keyword(
        session=db, keyword=category.keywords[0].keyword
    )

    assert result is not None
    assert result.id == category.id


def test_get_category_by_keyword_not_found(db: Session):
    category = create_random_category_with_keywords(db)
    result = crud.get_category_by_keyword(session=db, keyword="Empty Keyword")

    assert result is None
