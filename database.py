from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable not set")
if not MONGO_URI.startswith("mongodb"):
    raise ValueError("MONGO_URI is not a valid MongoDB connection string")

client = AsyncIOMotorClient(MONGO_URI)
db = client.todo_db  # Database name: todo_db
collection = db.todos  # Collection name: todos