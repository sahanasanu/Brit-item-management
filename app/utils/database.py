from pymongo import MongoClient
from pymongo.database import Database
from app.config import settings

# Create a MongoDB client
client = MongoClient(settings.MONGO_URI)

# Access the specific database
db = client[settings.DATABASE_NAME]

# Function to get the database
def get_db() -> Database:
    return db
