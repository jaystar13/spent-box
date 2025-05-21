# app/models/user_model.py

from datetime import datetime
import uuid

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class User(Base):
    # __tablename__ = "users"

    # id: Mapped[uuid.UUID] = mapped_column(
    #     UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    # )
    # email: Mapped[str] = mapped_column(String, nullable=False)
    # password: Mapped[str] = mapped_column(String, nullable=False)
    # created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, index=True)
