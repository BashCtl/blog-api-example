from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import verify_password
from app.models.account_model import Account
from app.schemas.token_schema import Token
from app.services.auth_service import AuthService

auth_router = APIRouter()


@auth_router.post("/login", response_model=Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.email == request.username).first()
    if not account:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
    if not verify_password(request.password, account.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
    access_token = AuthService.create_access_token({"id": account.id})

    return {"token_type": "bearer", "access_token": access_token}
