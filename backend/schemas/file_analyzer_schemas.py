from typing import Optional
from pydantic import BaseModel


class FileAnalyzeRequest(BaseModel):
    institution: str
    user_id: int
    year: Optional[int] = None
    month: Optional[int] = None
