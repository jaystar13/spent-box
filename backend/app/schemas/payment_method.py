from typing import Optional
import uuid
from sqlmodel import Field, SQLModel


class PaymentMethodBase(SQLModel):
    name: str = Field(max_length=100)
    type: str = Field(max_length=100)
    billing_day: Optional[int] = Field(default=None)


class PaymentMethodCreate(PaymentMethodBase):
    pass


class PaymentMethodUpdate(SQLModel):
    name: Optional[str] = None
    type: Optional[str] = None
    billing_day: Optional[int] = None


class PaymentMethodRead(PaymentMethodBase):
    id: uuid.UUID
