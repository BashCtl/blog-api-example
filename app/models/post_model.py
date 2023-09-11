from . import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))
    author_id = Column(Integer, ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False)
    author = relationship("Account")
