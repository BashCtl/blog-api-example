from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.models.account_model import Account
from app.schemas import post_schema
from app.core.database import get_db
from app.services.auth_service import AuthService
from app.services.post_service import PostService

posts_router = APIRouter()


@posts_router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(data: post_schema.Post, db: Session = Depends(get_db),
                current_account: Account = Depends(AuthService.get_current_user)):
    new_post = PostService.create_post(data, current_account, db)
    return new_post
