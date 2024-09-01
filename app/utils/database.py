from pymongo import MongoClient
from pymongo.database import Database
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Create a MongoDB client
client = MongoClient(MONGO_URI)

# Access the specific database
db = client[DATABASE_NAME]

# Function to get the database
def get_db() -> Database:
    return db
