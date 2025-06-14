from sqlmodel import Session

from app.tests.utils.user import create_random_user
from app.schemas import PaymentMethodCreate
from app import crud


def create_random_payment_method(db: Session):
    user = create_random_user(db)
    user_id = user.id
    assert user_id is not None
    payment_method_in = PaymentMethodCreate(
        name="KB카드", type="신용카드", billing_day=12
    )
    return crud.create_payment_method(db, user, payment_method_in)
