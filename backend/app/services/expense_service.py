from app.models.expense import (
    MonthlyExpenseRequest,
    MonthlyExpenseResponse,
    MonthlyExpenses,
)


def save_monthly_expense(user_id: int, payload: MonthlyExpenseRequest):
    # 나중에 DB 저장 로직으로 교체
    print(f"👤 user_id={user_id}, 저장 요청: {payload}")
    # 예: db.insert_monthly_expense(user_id, payload)
    saved_data = MonthlyExpenses(
        year=payload.year, month=payload.month, expenses=payload.expenses
    )
    return MonthlyExpenseResponse(message="저장 완료", data=saved_data)
