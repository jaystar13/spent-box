async def get_user_categories(user_id: str):
    return [
        {"category": "식비", "items": ["스타벅스", "맥도날드", "프레디버거"]},
        {"category": "쇼핑", "items": ["무신사", "11번가"]},
        {"category": "교통", "items": ["카카오택시", "버스"]},
    ]
