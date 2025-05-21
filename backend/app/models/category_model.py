from datetime import datetime
import uuid

from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    color: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    keywords: Mapped[list["CategoryKeyword"]] = relationship(
        "CategoryKeyword", back_populates="category", cascade="all, delete"
    )


class CategoryKeyword(Base):
    __tablename__ = "category_keywords"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("categories.id"), nullable=False
    )
    keyword: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    category: Mapped["Category"] = relationship("Category", back_populates="keywords")
