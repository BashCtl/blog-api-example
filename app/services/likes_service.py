from fastapi import HTTPException, status, Response
from app.schemas import post_schema
from sqlalchemy.orm import Session
from app.models.post_model import Post
from app.models.account_model import Account
from app.models.post_like_model import PostLike


class LikeService:

    @staticmethod
    def set_post_like(post_id: int, account: Account, db: Session):
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id '{post_id}' not found.")

        post_like_query = db.query(PostLike).filter(PostLike.post_id == post_id, PostLike.author_id == account.id)
        if not post_like_query.first():
            post_like = PostLike(post_id=post_id, author_id=account.id)
            db.add(post_like)
            db.commit()
            return {"message": "Successfully added like."}
        else:
            post_like_query.delete(synchronize_session=False)
            db.commit()
            return {"message": "Successfully removed like."}
