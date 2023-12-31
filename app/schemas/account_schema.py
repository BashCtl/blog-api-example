from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Account(BaseModel):
    email: EmailStr = Field(..., description="user email")
    name: str = Field(..., min_length=2, max_length=55, description="user name")
    password: str = Field(..., min_length=5, max_length=20, description="user password")


class AccountOut(BaseModel):
    id: int
    name: str
    email: EmailStr


class AccountIn(BaseModel):
    email: EmailStr
    password: str


class AccountUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
