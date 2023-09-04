from fastapi import HTTPException, status, Response
from app.schemas import comment_schema
from sqlalchemy.orm import Session
from app.models.comments_model import Comment
from app.models.account_model import Account
from app.models.post_model import Post


class CommentService:

    @staticmethod
    def create_comment(post_id: int, data: comment_schema.CommentIn, user: Account, db: Session):
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id '{post_id}' not found.")
        new_comment = Comment(post_id=post_id, author_id=user.id, **data.model_dump())
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)
        return new_comment

    @staticmethod
    def get_all_comments_for_post(post_id: int, db: Session):
        comments = db.query(Comment).filter(Comment.post_id == post_id).all()
        return comments

    @staticmethod
    def get_comment_by_id(comment_id: int, db: Session):
        comment = db.query(Comment).filter(Comment.id == comment_id).first()
        if not comment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Comment with id '{comment_id}' not found.")
        return comment

    @staticmethod
    def update_comment(comment_id: int, data: comment_schema.CommentIn, account: Account, db: Session):
        comment_query = CommentService.__get_author_comment_query(comment_id, account.id, db)
        comment_query.update(data.model_dump(), synchronize_session=False)
        db.commit()
        return comment_query.first()

    @staticmethod
    def delete_comment(comment_id: int, account: Account, db: Session):
        comment_query = CommentService.__get_author_comment_query(comment_id, account.id, db)
        comment_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def __get_author_comment_query(comment_id: int, account_id: int, db: Session):
        comment_query = db.query(Comment).filter(Comment.id == comment_id, Comment.author_id == account_id)
        if not comment_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Comment with id '{comment_id}' not found.")
        return comment_query
