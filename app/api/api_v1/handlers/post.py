from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.models.account_model import Account
from app.schemas import post_schema
from app.core.database import get_db
from app.services.auth_service import AuthService
from app.services.post_service import PostService

posts_router = APIRouter()


@posts_router.post("/", status_code=status.HTTP_201_CREATED, response_model=post_schema.PostOut)
def create_post(data: post_schema.Post, db: Session = Depends(get_db),
                current_account: Account = Depends(AuthService.get_current_user)):
    new_post = PostService.create_post(data, current_account, db)
    return new_post


@posts_router.get("/", response_model=List[post_schema.PostOut])
def get_all(current_account: Account = Depends(AuthService.get_current_user), db: Session = Depends(get_db)):
    posts = PostService.get_all_posts(current_account, db)
    return posts


@posts_router.get("/{id}", response_model=post_schema.PostOut)
def get_post(id: int, current_account: Account = Depends(AuthService.get_current_user),
             db: Session = Depends(get_db)):
    post = PostService.get_post_by_id(id, current_account, db)
    return post


@posts_router.put("/{id}", status_code=status.HTTP_201_CREATED, response_model=post_schema.PostOut)
def update_post(id: int, post: post_schema.Post, current_account: Account = Depends(AuthService.get_current_user),
                db: Session = Depends(get_db)):
    updated_post = PostService.update_post(id, post, current_account, db)
    return updated_post


@posts_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, current_account: Account = Depends(AuthService.get_current_user),
                db: Session = Depends(get_db)):
    return PostService.delete_post(id, current_account, db)
