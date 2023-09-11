from sqlalchemy import Column, Integer, ForeignKey

from . import Base


class CommentLike(Base):
    __tablename__ = "comment_likes"
    author_id = Column(Integer, ForeignKey("accounts.id", ondelete="CASCADE"), primary_key=True)
    comment_id = Column(Integer, ForeignKey("comments.id", ondelete="CASCADE"), primary_key=True)
