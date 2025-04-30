from fastapi import APIRouter
from backend.api.endpoints import expenses, upload

router = APIRouter()

# 각 도메인별 라우터 등록
router.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])
router.include_router(upload.router, prefix="/upload")


@router.get("/health")
async def health_check():
    return {"status": "ok"}
