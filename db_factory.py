from fastapi import HTTPException
from models.log_request_entity import LogRequestEntity
from abc import ABC, abstractmethod
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
connection_string = os.getenv("CONNECTION_STRING")

class IDatabase(ABC):
    @abstractmethod
    def initialise(self):
        pass

    @abstractmethod
    def insert_log(self):
        pass


class DatabaseFactory:
    def __init__(self, uri):
        self.uri = uri

    def get_database(key) -> IDatabase:
        if key.lower() == 'mongodb':
            db = MongodbDatabase()
        else:
            db =  MongodbDatabase()

class MongodbDatabase(IDatabase):
    def initialise(self, connection_string, level):
        self.connection_string = connection_string
        try:
            self.client = AsyncIOMotorClient(connection_string)
            self.db = self.client['logs']
            self.collection = self.db[f"logs_{self.level}"]
            print("******MongoDB connection successful.******")
        except Exception as e:
            print(f"Connection failed: {str(e)}")

    async def insert_log(self, log:LogRequestEntity):
        try:
            result = await self.collection.insert_one(log)
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error inserting log: {str(e)}")

    async def delete_log(self, log_id: str):
        return self._db.delete_one(log_id)
        