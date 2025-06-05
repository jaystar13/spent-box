from datetime import datetime
import uuid
from sqlmodel import Field, Relationship
from typing import Optional, TYPE_CHECKING

from app.schemas.category_keyword import CategoryKeywordBase

if TYPE_CHECKING:
    from .category import Category


class CategoryKeyword(CategoryKeywordBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    category_id: uuid.UUID = Field(foreign_key="category.id")
    keyword: str
    created_at: datetime = Field(default_factory=datetime.now)
    category: Optional["Category"] = Relationship(back_populates="keywords")
