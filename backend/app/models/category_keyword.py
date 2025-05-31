from datetime import datetime
import uuid
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .category import Category


class CategoryKeywordBase(SQLModel):
    keyword: str = Field(max_length=100)


class CategoryKeywordCreate(CategoryKeywordBase):
    category_id: uuid.UUID


class CategoryKeyword(CategoryKeywordBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    category_id: uuid.UUID = Field(foreign_key="category.id")
    created_at: datetime = Field(default_factory=datetime.now)
    category: Optional["Category"] = Relationship(back_populates="keywords")


class CategoryKeywordPublic(CategoryKeywordBase):
    id: uuid.UUID
    created_at: datetime
