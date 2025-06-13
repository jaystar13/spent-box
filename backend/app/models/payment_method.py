import uuid
from sqlmodel import Field
from app.schemas.payment_method import PaymentMethodBase


class PaymentMethod(PaymentMethodBase, table=True):
    __tablename__ = "payment_method"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
