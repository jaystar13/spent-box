from typing import Any
from fastapi import APIRouter, status

from app import crud
from app.api.deps import SessionDep, CurrentUser
from app.models import (
    CategoryCreate,
    CategoryPublic,
    CategoryWithKeywordsCreate,
    CategoryWithKeywordsPublic,
)

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


@router.post(
    "/with-keywords",
    response_model=CategoryWithKeywordsPublic,
    status_code=status.HTTP_201_CREATED,
)
def create_category_with_keywords(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    category_in: CategoryWithKeywordsCreate
) -> Any:
    return crud.create_category_with_keywords(
        session=session, current_user=current_user, data=category_in
    )
