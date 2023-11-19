
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os, pika
from datetime import datetime

load_dotenv()

CONNECTION_STRING = os.environ.get('CONNECTION_STRING')

client = AsyncIOMotorClient(CONNECTION_STRING)
db = client["Log_Ingestor"]

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
print("[✅] Connection over channel established")
channel = connection.channel()
channel.queue_declare(queue="logs")


def convert_to_unix_timestamp(iso_timestamp):
    iso_datetime = datetime.fromisoformat(iso_timestamp)
    unix_timestamp = int(iso_datetime.timestamp())
    return unix_timestamp

def convert_to_utc_timestamp(unix_timestamp):
    utc_timestamp = datetime.utcfromtimestamp(unix_timestamp)
    return utc_timestamp
