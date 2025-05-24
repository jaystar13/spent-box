from fastapi import APIRouter

from app.api.endpoints import user_api

router = APIRouter()

# router.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])
# router.include_router(upload.router, prefix="/upload")
# router.include_router(categories.router, prefix="/categories")
router.include_router(user_api.router, prefix="/users")
