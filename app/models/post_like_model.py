from sqlalchemy import Column, Integer, ForeignKey

from . import Base


class PostLike(Base):
    __tablename__ = "post_likes"
    author_id = Column(Integer, ForeignKey("accounts.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
