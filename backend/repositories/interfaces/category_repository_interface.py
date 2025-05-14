from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from models import Category


class ICategoryRepository(ABC):

    @abstractmethod
    def create_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    def add_keywords(self, category_id: UUID, keywords: List[str]):
        pass

    @abstractmethod
    def get_all_by_user(self, user_id: UUID) -> List[Category]:
        pass

    @abstractmethod
    def get_by_id_and_user(
        self, category_id: UUID, user_id: UUID
    ) -> Optional[Category]:
        pass

    @abstractmethod
    def update_category(self, category: Category):
        pass

    @abstractmethod
    def delete_keywords(self, category_id: UUID):
        pass

    @abstractmethod
    def delete_category(self, category: Category):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def refresh(self, instance):
        pass
