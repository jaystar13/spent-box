import pytest

from app.models.expense import MonthlyExpenseRequest
from app.services.expense_service import save_monthly_expense


@pytest.fixture
def sample_request():
    return MonthlyExpenseRequest(
        year=2025,
        month=4,
        expenses=[
            {"category": "식비", "amount": 30000},
            {"category": "교통비", "amount": 100000},
        ],
    )


def test_save_monthly_expense(sample_request):
    user_id = 1
    result = save_monthly_expense(user_id, sample_request)

    assert result.message == "저장 완료"
    assert result.data.year == 2025
    assert result.data.month == 4
    assert len(result.data.expenses) == 2
    assert result.data.expenses[0].category == "식비"
    assert result.data.expenses[0].amount == 30000
