from datetime import datetime
from pydantic import BaseModel
from . import account_schema


class PostIn(BaseModel):
    title: str
    body: str


class Post(PostIn):
    id: int
    title: str
    body: str
    created_at: datetime
    author: account_schema.AccountOut


class PostOut(BaseModel):
    Post: Post
    likes: int = 0
