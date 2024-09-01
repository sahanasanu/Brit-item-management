from passlib.context import CryptContext
from pymongo.collection import Collection
from app.schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def create_user(user: UserCreate, collection: Collection) -> dict:
    """
    Create a new user and store it in the database.
    """
    hashed_password = get_password_hash(user.password)
    db_user = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password
    }
    result = await collection.insert_one(db_user)
    db_user["_id"] = result.inserted_id
    return db_user

async def authenticate_user(username: str, password: str, collection: Collection) -> dict:
    """
    Authenticate a user by verifying the password.
    """
    user = await collection.find_one({"username": username})
    if user and verify_password(password, user["hashed_password"]):
        return user
    return None
