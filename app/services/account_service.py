from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas import account_schema
from app.core.security import hashing_password
from app.models.account_model import Account


class AccountService:

    @staticmethod
    def create_account(body: account_schema.Account, db: Session):
        body.password = hashing_password(body.password)
        new_account = Account(**body.model_dump())
        db.add(new_account)
        db.commit()
        db.refresh(new_account)
        return new_account

    @staticmethod
    def get_account(id: int, db: Session):
        account = db.query(Account).filter(Account.id == id).first()
        if not account:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Account with id '{id}' not found.")
        return account

    @staticmethod
    def update_account(body: account_schema.AccountUpdate, account: Account, db: Session):
        update_account = AccountService.get_account(account.id, db)
        if db.query(Account).filter(Account.email == body.email).first() and body.email != account.email:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"Account with provided email already exists.")
        if body.email:
            update_account.email = body.email
        if body.name:
            update_account.name = body.name
        db.commit()
        return update_account
