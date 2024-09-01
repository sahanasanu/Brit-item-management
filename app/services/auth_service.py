from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models import User
from app.schemas import UserCreate
from fastapi import Depends

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(user: UserCreate, db: Session = Depends(get_db)):
    #hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    #if user and verify_password(password, user.hashed_password):
    if user and password:
        return user
    return None
