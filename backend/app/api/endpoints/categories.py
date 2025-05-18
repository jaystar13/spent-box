from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.category_schema import CategoryCreate, CategoryRead
from app.services.category_service import CategoryService
from app.deps.auth import get_current_user_id
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=CategoryRead)
def create_category(
    data: CategoryCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user_id),
):
    return CategoryService.create_category(db, user.id, data)
