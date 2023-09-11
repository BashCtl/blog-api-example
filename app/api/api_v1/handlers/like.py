from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.account_model import Account
from app.schemas import post_schema
from app.core.database import get_db
from app.services.auth_service import AuthService
from app.services.likes_service import LikeService

likes_router = APIRouter()


@likes_router.post("/likes/posts/<post_id>", status_code=status.HTTP_201_CREATED)
def set_like_for_post(post_id: int, current_account: Account = Depends(AuthService.get_current_user),
                      db: Session = Depends(get_db)):
    return LikeService.set_post_like(post_id, current_account, db)


@likes_router.post("/likes/comments/<comment_id>", status_code=status.HTTP_201_CREATED)
def set_like_for_comment(comment_id: int, current_account: Account = Depends(AuthService.get_current_user),
                         db: Session = Depends(get_db)):
    return LikeService.set_comment_like(comment_id, current_account, db)
