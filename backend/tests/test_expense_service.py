import pytest

from backend.models.expense import MonthlyExpenseRequest
from backend.services.expense_service import save_monthly_expense


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

    assert result.year == 2025
    assert result.month == 4
    assert len(result.expenses) == 2
    assert result.expenses[0].category == "식비"
    assert result.expenses[0].amount == 30000
