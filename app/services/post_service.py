from fastapi import HTTPException, status, Response
from app.schemas import post_schema
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.post_model import Post
from app.models.account_model import Account
from app.models.post_like_model import PostLike


class PostService:

    @staticmethod
    def create_post(data: post_schema.PostIn, account: Account, db: Session):
        new_post = Post(author_id=account.id, **data.model_dump())
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post

    @staticmethod
    def get_all_account_posts(account: Account, db: Session, limit: int, skip: int):
        posts = db.query(Post, func.count(PostLike.post_id).label("likes")) \
            .join(PostLike, PostLike.post_id == Post.id, isouter=True) \
            .group_by(Post.id).filter(Post.author_id == account.id).limit(limit).offset(skip).all()
        posts = list(map(lambda p: p._mapping, posts))
        return posts

    @staticmethod
    def get_post_by_id(id: int, account: Account, db: Session):
        post = db.query(Post, func.count(PostLike.post_id).label("likes"))\
                .join(PostLike, PostLike.post_id==id)\
                .group_by(Post.id)\
                .filter(Post.id == id, Post.author_id == account.id).first()
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id '{id}' not found.")
        return post

    @staticmethod
    def update_post(id: int, post: post_schema.PostIn, account: Account, db: Session):
        post_query = db.query(Post).filter(Post.id == id, Post.author_id == account.id)
        if not post_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id '{id}' not found.")
        post_query.update(post.model_dump(), synchronize_session=False)
        db.commit()
        return post_query.first()

    @staticmethod
    def delete_post(id: int, account: Account, db: Session):
        post_query = db.query(Post).filter(Post.id == id, Post.author_id == account.id)
        if not post_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id '{id}' not found.")
        post_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
