from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.models.account_model import Account
from app.schemas import post_schema, comment_schema
from app.core.database import get_db
from app.services.auth_service import AuthService
from app.services.comment_service import CommentService

comments_router = APIRouter()


@comments_router.post("/{post_id}", response_model=comment_schema.CommentOut,
                      status_code=status.HTTP_201_CREATED)
def create_comment(post_id: int, data: comment_schema.CommentIn,
                   current_account: Account = Depends(AuthService.get_current_user),
                   db: Session = Depends(get_db)):
    return CommentService.create_comment(post_id, data, current_account, db)


@comments_router.get("/post/{post_id}", response_model=List[comment_schema.CommentOut])
def get_all_post_comments(post_id: int, account: Account = Depends(AuthService.get_current_user),
                          db: Session = Depends(get_db)):
    return CommentService.get_all_comments_for_post(post_id, db)


@comments_router.get("/{comment_id}", response_model=comment_schema.CommentOut)
def get_comment(comment_id: int, account: Account = Depends(AuthService.get_current_user),
                db: Session = Depends(get_db)):
    return CommentService.get_comment_by_id(comment_id, db)


@comments_router.put("/{comment_id}", response_model=comment_schema.CommentOut)
def update_comment(comment_id: int, data: comment_schema.CommentIn,
                   account: Account = Depends(AuthService.get_current_user), db: Session = Depends(get_db)):
    return CommentService.update_comment(comment_id, data, account, db)


@comments_router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id: int, account: Account = Depends(AuthService.get_current_user),
                   db: Session = Depends(get_db)):
    return CommentService.delete_comment(comment_id, account, db)
