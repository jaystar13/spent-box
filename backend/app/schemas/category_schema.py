from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel


class CategoryKeywordCreate(BaseModel):
    keyword: str


class CategoryKeywordRead(CategoryKeywordCreate):
    id: UUID
    created_at: datetime


class CategoryBase(BaseModel):
    name: str
    color: str


class CategoryCreate(CategoryBase):
    keywords: Optional[List[CategoryKeywordCreate]] = []


class CategoryRead(CategoryBase):
    id: UUID
    created_at: datetime
    keywords: List[CategoryKeywordRead] = []


class CategoryUpdate(BaseModel):
    name: Optional[str]
    color: Optional[str]
    keywords: Optional[List[CategoryKeywordCreate]]
