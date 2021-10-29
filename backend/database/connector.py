from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from decouple import config


connection_url = config("MONGO_DETAILS")

client = AsyncIOMotorClient(connection_url)
engine = AIOEngine(motor_client=client, database="google-bsn-task")