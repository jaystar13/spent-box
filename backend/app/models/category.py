import uuid
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .category_keyword import CategoryKeyword


class CategoryBase(SQLModel):
    name: str = Field(max_length=100)
    color: str = Field(max_length=20)


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.now)
    keywords: List["CategoryKeyword"] = Relationship(
        back_populates="category", sa_relationship_kwargs={"cascade": "all, delete"}
    )


class CategoryPublic(CategoryBase):
    id: uuid.UUID
    created_at: datetime
