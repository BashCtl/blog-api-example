from jose import jwt, JWTError
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from app.core.configs import settings
from app.schemas.token_schema import TokenData
from app.core.database import get_db
from app.models.account_model import Account


class AuthService:
    SECRET_KEY = settings.SECRET_KEY
    ALGORITHM = settings.ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

    @staticmethod
    def create_access_token(data: dict):
        to_encode = data.copy()

        expire = datetime.utcnow() + timedelta(minutes=AuthService.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, AuthService.SECRET_KEY, algorithm=AuthService.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verify_access_token(token: str, credential_exception):
        try:
            payload = jwt.decode(token, AuthService.SECRET_KEY, algorithms=[AuthService.ALGORITHM])
            id: int = payload.get("id")
            if id is None:
                raise credential_exception
            toke_data = TokenData(id=id)
        except JWTError:
            raise credential_exception
        return toke_data

    @staticmethod
    def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
        credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                             detail="Could not validate credentials",
                                             headers={"WWW-Authenticate": "Bearer"})
        token = AuthService.verify_access_token(token, credential_exception)
        account = db.query(Account).filter(Account.id == token.id).first()
        return account
