import uuid
from datetime import datetime
from sqlmodel import Field, Relationship
from typing import List, TYPE_CHECKING

from app.schemas.category import CategoryBase

if TYPE_CHECKING:
    from .category_keyword import CategoryKeyword


class Category(CategoryBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.now)
    keywords: List["CategoryKeyword"] = Relationship(
        back_populates="category", sa_relationship_kwargs={"cascade": "all, delete"}
    )
