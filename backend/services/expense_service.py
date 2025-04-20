from models.expense import MonthlyExpenseRequest


def save_monthly_expense(user_id: int, payload: MonthlyExpenseRequest):
    # 나중에 DB 저장 로직으로 교체
    print(f"👤 user_id={user_id}, 저장 요청: {payload}")
    # 예: db.insert_monthly_expense(user_id, payload)
    return payload
