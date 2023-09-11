from datetime import datetime
from pydantic import BaseModel
from ..schemas import account_schema, post_schema


class CommentIn(BaseModel):
    body: str


class CommentOut(BaseModel):
    id: int
    body: str
    created_at: datetime
    post: post_schema.PostOut
    likes: int
