from app.schemas import account_schema
from sqlalchemy.orm import Session
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
