from fastapi import APIRouter, Depends
from backend.models.expense import MonthlyExpenseRequest, MonthlyExpenseResponse
from backend.services.expense_service import save_monthly_expense

router = APIRouter()


# TODO: 실제 인증 시스템 붙이면 여기에 사용
def get_current_user_id():
    return 1  # 샘플: 인증된 사용자 ID


@router.post("/monthly", response_model=MonthlyExpenseResponse)
def create_monthly_expense(
    payload: MonthlyExpenseRequest, user_id: int = Depends(get_current_user_id)
):
    return save_monthly_expense(user_id, payload)
