from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class ItemCreate(BaseModel):
    name: str
    price: int

class ItemResponse(BaseModel):
    id: int
    name: str
    owner_id: int
    price:int

    class Config:
        orm_mode = True
