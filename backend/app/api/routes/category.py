from typing import Any
from fastapi import APIRouter, Depends, HTTPException

from app import crud
from app.api.deps import SessionDep
from app.models import CategoryCreate, CategoryPublic

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post(
    "/",
    response_model=CategoryPublic,
)
def create_category(*, session: SessionDep, category_in: CategoryCreate) -> Any:
    """
    Create new category.
    """
    category = crud.create_category(session=session, category_in=category_in)
    return category
