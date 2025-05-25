from typing import Any
from fastapi import APIRouter, Depends, HTTPException

from app import crud
from app.core.config import settings
from app.api.deps import SessionDep, get_current_active_superuser
from app.models2 import UserCreate, UserPublic
from app.utils import generate_new_account_email, send_email


router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=UserPublic,
)
def create_user(*, session: SessionDep, user_in: UserCreate) -> Any:
    """
    Create new user.
    """
    user = crud.get_user_by_email(session=session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    user = crud.create_user(session=session, user_create=user_in)

    if settings.emails_enabled and user_in.email:
        email_data = generate_new_account_email(
            email_to=user_in.email, username=user_in.email, password=user_in.password
        )

        send_email(
            email_to=user_in.email,
            subject=email_data.subject,
            html_content=email_data.html_content,
        )

        return user
