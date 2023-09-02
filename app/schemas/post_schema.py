from datetime import datetime
from pydantic import BaseModel
from . import account_schema


class Post(BaseModel):
    title: str
    body: str


class PostOut(BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime
    author: account_schema.AccountOut
