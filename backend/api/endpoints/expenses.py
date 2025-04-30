from fastapi import APIRouter, Depends
from backend.models.expense import MonthlyExpenseRequest, MonthlyExpenseResponse
from backend.services.expense_service import save_monthly_expense
from backend.deps.auth import get_current_user_id

router = APIRouter()


@router.post("/monthly", response_model=MonthlyExpenseResponse)
def create_monthly_expense(
    payload: MonthlyExpenseRequest, user_id: int = Depends(get_current_user_id)
):
    return save_monthly_expense(user_id, payload)
