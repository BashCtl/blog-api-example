from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas import account_schema
from app.core.database import get_db
from app.services.account_service import AccountService

account_router = APIRouter()


@account_router.post("/", response_model=account_schema.AccountOut,
                     status_code=status.HTTP_201_CREATED)
def create_account(body: account_schema.Account, db: Session = Depends(get_db)):
    new_account = AccountService.create_account(body, db)
    return new_account
