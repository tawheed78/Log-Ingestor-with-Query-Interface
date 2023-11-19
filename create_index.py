import asyncio
from pymongo import ASCENDING, TEXT
from config import db

collection = db['logs']
async def create_indexes():
    await collection.create_index([("level", ASCENDING)])
    await collection.create_index([("timestamp", ASCENDING)])
    await collection.create_index([("message", TEXT)])
    await collection.create_index([("resourceId", ASCENDING)])
    print("Indexes created successfully")

loop = asyncio.get_event_loop()
loop.run_until_complete(create_indexes())
loop.close()