from typing import List
import uuid
from fastapi import APIRouter, HTTPException

from app.schemas import (
    PaymentMethodRead,
    PaymentMethodCreate,
    PaymentMethodUpdate,
    PaymentMethodPublic,
)
from app.api.deps import CurrentUser, SessionDep
from app import crud

router = APIRouter(prefix="/payment-methods", tags=["결제수단"])


@router.get("/", response_model=List[PaymentMethodRead])
def list_payment_methods(session: SessionDep):
    return crud.get_all_payment_methods(session)


@router.get("/{payment_method_id}", response_model=PaymentMethodRead)
def get_payment_method(payment_method_id: uuid.UUID, session: SessionDep):
    result = crud.get_payment_method(session, payment_method_id)
    if not result:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return result


@router.post("/", response_model=PaymentMethodPublic)
def create_payment_method(
    data: PaymentMethodCreate, session: SessionDep, current_user: CurrentUser
):
    return crud.create_payment_method(session, current_user, data)


@router.put("/{payment_method_id}", response_model=PaymentMethodPublic)
def update_payment_method(
    payment_method_id: uuid.UUID, data: PaymentMethodUpdate, session: SessionDep
):
    updated = crud.update_payment_method(session, payment_method_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return updated


@router.delete("/{payment_method_id}")
def delete_payment_method(payment_method_id: uuid.UUID, session: SessionDep):
    deleted = crud.delete_payment_method(session, payment_method_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return {"ok": True}
