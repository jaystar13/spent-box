from typing import Any
import uuid
from fastapi import APIRouter, status

from app import crud
from app.api.deps import SessionDep, CurrentUser
from app.schemas import (
    CategoryPublic,
    CategoryCreate,
    CategoryWithKeywordsPublic,
    CategoryWithKeywordsCreate,
    CategoryDetailRead,
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


@router.get("/{category_id}", response_model=CategoryDetailRead)
def read_category_detail(category_id: uuid.UUID, session: SessionDep):
    return crud.get_category_with_keywords(session=session, category_id=category_id)
