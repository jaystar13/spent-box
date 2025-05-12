import pytest

from backend.services.categorization_service import ExpenseCategorizationService


@pytest.fixture
def category_data():
    return [
        {"category": "식비", "items": ["스타벅스", "맥도날드"]},
        {"category": "쇼핑", "items": ["무신사", "11번가"]},
        {"category": "교통", "items": ["카카오택시", "버스"]},
    ]


@pytest.fixture
def expenses():
    return [
        {"이용일자": "2025-05-01", "가맹정명": "스타벅스", "이용금액": 4500},
        {"이용일자": "2025-05-05", "가맹정명": "무신사", "이용금액": 30000},
        {"이용일자": "2025-05-10", "가맹정명": "버스", "이용금액": 1250},
        {
            "이용일자": "2025-04-30",
            "가맹정명": "스타벅스",
            "이용금액": 4000,
        },  # 월이 다름
        {"이용일자": "2025-05-15", "가맹정명": "기타상점", "이용금액": 9990},  # 미분류
    ]


def test_categorize(category_data, expenses):
    service = ExpenseCategorizationService(category_data)
    result = service.categorize(expenses, year=2025, month=5)

    # 결과를 카테고리별로 정리
    result_dict = {entry["category"]: entry for entry in result}

    assert len(result) == 4
    assert result_dict["식비"]["amount"] == 4500
    assert result_dict["쇼핑"]["amount"] == 30000
    assert result_dict["교통"]["amount"] == 1250
    assert result_dict["미분류"]["amount"] == 9990
    assert "기타상점" in result_dict["미분류"]["targetItems"]
