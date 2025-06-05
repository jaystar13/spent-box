import uuid
from datetime import datetime
from typing import List
from sqlmodel import SQLModel, Field
from pydantic import BaseModel


class CategoryKeywordBase(SQLModel):
    keyword: str = Field(max_length=100)


class CategoryKeywordCreate(CategoryKeywordBase):
    category_id: uuid.UUID


class CategoryKeywordPublic(CategoryKeywordBase):
    id: uuid.UUID
    created_at: datetime


class CategoryWithKeywordsCreate(BaseModel):
    name: str
    color: str
    keywords: List[str]
