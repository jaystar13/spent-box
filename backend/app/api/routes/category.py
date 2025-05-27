from typing import Any
from fastapi import APIRouter, Depends, HTTPException

from app import crud
from app.api.deps import SessionDep, CurrentUser
from app.models import CategoryCreate, CategoryPublic

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post(
    "/",
    response_model=CategoryPublic,
)
def create_category(
    *, session: SessionDep, current_user: CurrentUser, category_in: CategoryCreate
) -> Any:
    """
    Create new category.
    """
    return crud.create_category(
        session=session, current_user=current_user, category_in=category_in
    )
