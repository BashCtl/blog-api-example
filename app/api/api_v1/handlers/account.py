from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas import account_schema
from app.core.database import get_db
from app.services.account_service import AccountService
from app.models.account_model import Account
from app.services.auth_service import AuthService

account_router = APIRouter()


@account_router.post("/", response_model=account_schema.AccountOut,
                     status_code=status.HTTP_201_CREATED)
def create_account(body: account_schema.Account, db: Session = Depends(get_db)):
    new_account = AccountService.create_account(body, db)
    return new_account


@account_router.get("/{id}", response_model=account_schema.AccountOut)
def get_account(id: int, db: Session = Depends(get_db)):
    account = AccountService.get_account(id, db)
    return account


@account_router.patch("/", response_model=account_schema.AccountOut, status_code=status.HTTP_201_CREATED)
def update_account(body: account_schema.AccountUpdate,
                   current_account: Account = Depends(AuthService.get_current_user),
                   db: Session = Depends(get_db)):
    updated_account = AccountService.update_account(body, current_account, db)
    return updated_account
