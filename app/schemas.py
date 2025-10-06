from pydantic import BaseModel, EmailStr, Field
from typing import Literal

# Auth
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class UserOut(BaseModel):
    id: int
    email: EmailStr
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginIn(BaseModel):
    email: EmailStr
    password: str

# Categories
class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    type: Literal["income", "expense"] = "expense"

class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    type: Literal["income", "expense"] | None = None

class CategoryOut(BaseModel):
    id: int
    name: str
    type: Literal["income", "expense"]
    class Config:
        from_attributes = True
