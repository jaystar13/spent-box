import uuid
from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict
from sqlmodel import SQLModel, Field

from app.schemas.category_keyword import CategoryKeywordPublic


class CategoryBase(SQLModel):
    name: str = Field(max_length=100)
    color: str = Field(max_length=20)


class CategoryCreate(CategoryBase):
    pass


class CategoryPublic(CategoryBase):
    id: uuid.UUID
    created_at: datetime


class CategoryWithKeywordsPublic(CategoryPublic):
    keywords: List[CategoryKeywordPublic]

    model_config = ConfigDict(from_attributes=True)


CategoryWithKeywordsPublic.model_rebuild()


class CategoryKeywordRead(BaseModel):
    id: uuid.UUID
    keyword: str

    model_config = ConfigDict(from_attributes=True)


class CategoryDetailRead(BaseModel):
    id: uuid.UUID
    name: str
    keywords: List[CategoryKeywordRead]

    model_config = ConfigDict(from_attributes=True)
