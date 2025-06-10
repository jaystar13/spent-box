from app import crud


def test_categorize():
    user_categories = [
        {"category": "식비", "items": ["스타벅스", "맥도날드"]},
        {"category": "쇼핑", "items": ["무신사", "11번가"]},
        {"category": "교통", "items": ["카카오택시", "버스"]},
    ]
    spents = [
        {"date": "2025-05-01", "merchant": "스타벅스", "amount": 4500},
        {"date": "2025-05-05", "merchant": "무신사", "amount": 30000},
        {"date": "2025-05-10", "merchant": "버스", "amount": 1250},
        {
            "date": "2025-04-30",
            "merchant": "스타벅스",
            "amount": 4000,
        },  # 월이 다름
        {"date": "2025-05-15", "merchant": "기타상점", "amount": 9990},  # 미분류
    ]

    categorizer = crud.SpentListCategorizer(user_categories)
    result = categorizer.categorize(spents, year=2025, month=5)

    # 결과를 카테고리별로 정리
    result_dict = {entry["category"]: entry for entry in result}

    assert len(result) == 4
    assert result_dict["식비"]["amount"] == 4500
    assert result_dict["쇼핑"]["amount"] == 30000
    assert result_dict["교통"]["amount"] == 1250
    assert result_dict["미분류"]["amount"] == 9990
    assert "기타상점" in result_dict["미분류"]["targetItems"]


def test_partial_match_categorization():
    user_categories = [
        {"category": "식비", "items": ["스타벅스"]},
        {"category": "쇼핑", "items": ["무신사"]},
    ]
    spents = [
        {"date": "2025-05-01", "merchant": "(주)스타벅스 코리아", "amount": 5500},
        {"date": "2025-05-02", "merchant": "무신사스토어", "amount": 27000},
        {"date": "2025-05-03", "merchant": "기타상점", "amount": 9000},
    ]

    categorizer = crud.SpentListCategorizer(user_categories)
    result = categorizer.categorize(spents, year=2025, month=5)

    result_dict = {entry["category"]: entry for entry in result}

    assert result_dict["식비"]["amount"] == 5500
    assert result_dict["쇼핑"]["amount"] == 27000
    assert result_dict["미분류"]["amount"] == 9000
    assert "(주)스타벅스 코리아" in result_dict["식비"]["targetItems"]
    assert "무신사스토어" in result_dict["쇼핑"]["targetItems"]
