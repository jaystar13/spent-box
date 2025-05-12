from collections import defaultdict
from datetime import datetime
from typing import Dict, List


class ExpenseCategorizationService:
    def __init__(self, category_data: List[Dict]):
        self.item_to_category = self._build_category_map(category_data)

    def _build_category_map(self, cagegory_data: List[Dict]) -> Dict[str, str]:
        """카테고리 매핑 딕셔너리 생성"""
        item_to_category = {}
        for cat in cagegory_data:
            for item in cat["items"]:
                item_to_category[item] = cat["category"]
        return item_to_category

    def categorize(self, expenses: List[Dict], year: int, month: int) -> List[Dict]:
        """카드 사용내역을 카테고리별로 정리"""
        categorized = defaultdict(lambda: {"amount": 0, "targetItems": set()})

        for entry in expenses:
            entry_date = datetime.strptime(entry["이용일자"], "%Y-%m-%d")
            if entry_date.year != year or entry_date.month != month:
                continue

            store = entry["가맹정명"]
            amount = entry["이용금액"]
            category = self.item_to_category.get(store, "미분류")

            categorized[category]["amount"] += amount
            categorized[category]["targetItems"].add(store)

        result = []
        for idx, (category, data) in enumerate(categorized.items(), start=1):
            result.append(
                {
                    "id": idx,
                    "year": year,
                    "month": month,
                    "category": category,
                    "amount": data["amount"],
                    "targetItems": list(data["targetItems"]),
                }
            )

        return result
