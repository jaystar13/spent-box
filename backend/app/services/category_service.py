import uuid

from sqlalchemy.orm import Session
from app.models.category_model import Category, CategoryKeyword
from app.schemas.category_schema import CategoryCreate


class CategoryService:

    @staticmethod
    def create_category(
        db: Session, user_id: uuid.UUID, data: CategoryCreate
    ) -> Category:
        category = Category(
            user_id=user_id,
            name=data.name,
            color=data.color,
        )
        db.add(category)
        db.flush()

        for kw in data.keywords or []:
            keyword = CategoryKeyword(category_id=category.id, keyword=kw.keyword)
            db.add(keyword)

        db.commit()
        db.refresh(category)
        return category
