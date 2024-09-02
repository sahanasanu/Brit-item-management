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
    id: str
    username: str
    email: str

class ItemCreate(BaseModel):
    name: str
    price: int

class ItemResponse(BaseModel):
    id: str  # Change this to str to match MongoDB's ObjectId
    name: str
    price: float
    owner_id: str
