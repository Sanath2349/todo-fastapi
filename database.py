from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://sanathreddy:Reddy123@cluster0.ulqup.mongodb.net/")  # Default to local MongoDB if not set
client = AsyncIOMotorClient(MONGO_URI)
db = client.todo_db  # Database name: todo_db
collection = db.todos  # Collection name: todos