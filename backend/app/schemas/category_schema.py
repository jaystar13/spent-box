from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class CategoryKeywordCreate(BaseModel):
    keyword: str


class CategoryKeywordRead(CategoryKeywordCreate):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class CategoryBase(BaseModel):
    name: str
    color: str


class CategoryCreate(CategoryBase):
    keywords: Optional[List[CategoryKeywordCreate]] = []


class CategoryRead(CategoryBase):
    id: int
    created_at: datetime
    keywords: List[CategoryKeywordRead] = []
    model_config = ConfigDict(from_attributes=True)


class CategoryUpdate(BaseModel):
    name: Optional[str]
    color: Optional[str]
    keywords: Optional[List[CategoryKeywordCreate]]
