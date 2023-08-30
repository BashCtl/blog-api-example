from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas import account_schema
from app.core.database import get_db
from app.core.security import hashing_password
from app.models.account_model import Account

account_router = APIRouter()


@account_router.post("/", response_model=account_schema.AccountOut, status_code=status.HTTP_201_CREATED)
def create_account(body: account_schema.Account, db: Session = Depends(get_db)):
    body.password = hashing_password(body.password)
    new_account = Account(**body.model_dump())
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account
