from fastapi import APIRouter
from .handlers import account
from .handlers import auth

router = APIRouter()

router.include_router(account.account_router, prefix="/accounts", tags=["accounts"])
router.include_router(auth.auth_router,tags=["auth"])
