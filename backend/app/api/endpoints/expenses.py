from fastapi import APIRouter, Depends
from app.models.expense import MonthlyExpenseRequest, MonthlyExpenseResponse
from app.services.expense_service import save_monthly_expense
from app.deps.auth import get_current_user_id

router = APIRouter()


@router.post("/monthly", response_model=MonthlyExpenseResponse)
def create_monthly_expense(
    payload: MonthlyExpenseRequest, user_id: int = Depends(get_current_user_id)
):
    return save_monthly_expense(user_id, payload)
