from fastapi import APIRouter

from app.api.endpoints import expenses, upload

router = APIRouter()

router.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])
router.include_router(upload.router, prefix="/upload")
