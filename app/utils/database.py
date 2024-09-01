from pymongo import MongoClient
from pymongo.collection import Collection
from fastapi import Depends
from app.config import settings

# Create a MongoDB client
client = MongoClient(settings.MONGO_URI)

# Access the specific database
db = client[settings.DATABASE_NAME]

# Function to get the collection from the database
def get_collection() -> Collection:
    return db[settings.COLLECTION_NAME]
