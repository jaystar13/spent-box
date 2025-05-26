from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .category import Category


class CategoryKeywordBase(SQLModel):
    keyword: str = Field(max_length=100)


class CategoryKeywordCreate(CategoryKeywordBase):
    category_id: int


class CategoryKeyword(CategoryKeywordBase, table=True):
    id: int = Field(default=None, primary_key=True)
    category_id: int = Field(foreign_key="category.id")
    created_at: datetime = Field(default_factory=datetime.now)
    category: Optional["Category"] = Relationship(back_populates="keywords")


class CategoryKeywordPublic(CategoryKeywordBase):
    id: int
    created_at: datetime
