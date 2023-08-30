from fastapi import APIRouter
from .handlers import account

router = APIRouter()

router.include_router(account.account_router, prefix="/accounts", tags=["accounts"])
