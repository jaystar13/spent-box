from app.database import Base
from app.schemas.category_schema import CategoryCreate
from app.services.category_service import create_category


def test_create_category(db, test_user_id):
    category = CategoryCreate(
        name="식비",
        color="#FF5733",
        keywords=[
            {"keyword": "배달"},
            {"keyword": "편의점"},
        ],
    )
    result = create_category(db, test_user_id, category)

    assert result.name == "식비"
    assert len(result.keywords) == 2
