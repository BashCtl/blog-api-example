from app.schemas import post_schema
from sqlalchemy.orm import Session
from app.models.post_model import Post
from app.models.account_model import Account


class PostService:

    @staticmethod
    def create_post(data: post_schema.Post, account: Account, db: Session):
        new_post = Post(author_id=account.id, **data.model_dump())
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post
