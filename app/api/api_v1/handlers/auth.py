from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.account_model import Account
from app.services.auth_service import AuthService
from app.schemas import account_schema
from app.schemas.token_schema import Token
from app.core.security import verify_password

auth_router = APIRouter()


@auth_router.post("/login", response_model=Token)
def login(request: account_schema.AccountIn, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.email == request.email).first()
    if not account:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
    if not verify_password(request.password, account.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
    access_token = AuthService.create_access_token({"id": account.id})

    return {"token_type": "bearer", "access_token": access_token}
