import json
import os, sys
from dotenv import load_dotenv
from config import convert_to_unix_timestamp, db, channel, connection

load_dotenv()

collection = db['logs']
channel = connection.channel() 
channel.queue_declare(queue="logs_queue")


def callback(ch, method, properties, body):
    try:
        log_dict = json.loads(body.decode())
        timestamp = convert_to_unix_timestamp(log_dict['timestamp'])
        log_dict['timestamp'] = timestamp
        collection.insert_one(log_dict)
        print(f"[✅] Received: {log_dict}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Error: {e}")

channel.basic_consume(
    "logs_queue",
    callback,
    auto_ack=True,
)

try:
  print("\n[❎] Waiting for messages. To exit press CTRL+C \n")
  channel.start_consuming()
except Exception as e:
  print(f"Error: #{e}")
  try:
    sys.exit(0)
  except SystemExit:
    os._exit(0)

