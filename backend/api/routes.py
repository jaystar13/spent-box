from fastapi import APIRouter
from api.endpoints import expenses

router = APIRouter()

# 각 도메인별 라우터 등록
router.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])


@router.get("/health")
async def health_check():
    return {"status": "ok"}
