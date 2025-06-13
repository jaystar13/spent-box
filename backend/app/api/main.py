from fastapi import APIRouter

from app.core.config import settings
from app.api.routes import login, users, private, category, payment_method

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(category.router)
api_router.include_router(payment_method.router)

if settings.ENVIRONMENT == "local":
    api_router.include_router(private.router)
