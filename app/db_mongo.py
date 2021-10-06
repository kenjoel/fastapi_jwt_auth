import motor.motor_asyncio
from fastapi_users.db import MongoDBUserDatabase
from authentication.Models import UserDB

Database_url = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(Database_url, uuidRepresentation="standard")

db = client["db_name"]

collections = db["users"]


def get_user_db():
    yield MongoDBUserDatabase(UserDB, collections)
