from pydantic import BaseModel, EmailStr, Field


class Account(BaseModel):
    email: EmailStr = Field(..., description="user email")
    name: str = Field(..., min_length=2, max_length=55, description="user name")
    password: str = Field(..., min_length=5, max_length=20, description="user password")


class AccountOut(BaseModel):
    id: int
    name: str
    email: EmailStr
