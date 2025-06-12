import uuid

from sqlmodel import Field
from backend.app.schemas.payment_method import PaymentMethodBase


class PaymentMethod(PaymentMethodBase, table=True):
    __tablename__ = "payment_method"
