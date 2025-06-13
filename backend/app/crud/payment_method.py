from typing import List, Optional
import uuid
from sqlmodel import Session, select

from app.models.payment_method import PaymentMethod
from app.schemas.payment_method import PaymentMethodCreate, PaymentMethodUpdate


def get_all_payment_methods(session: Session) -> List[PaymentMethod]:
    result = session.exec(select(PaymentMethod))
    return result.all()


def get_payment_method(
    session: Session, payment_method_id: uuid.UUID
) -> Optional[PaymentMethod]:
    return session.get(PaymentMethod, payment_method_id)


def create_payment_method(session: Session, data: PaymentMethodCreate) -> PaymentMethod:
    item = PaymentMethod.model_validate(data)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def update_payment_method(
    session: Session, payment_method_id: uuid.UUID, data: PaymentMethodUpdate
) -> Optional[PaymentMethod]:
    item = session.get(PaymentMethod, payment_method_id)
    if not item:
        return None

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(item, key, value)

    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def delete_payment_method(session: Session, payment_method_id: uuid.UUID) -> bool:
    item = session.get(PaymentMethod, payment_method_id)
    if not item:
        return False

    session.delete(item)
    session.commit()
    return True
