
import json
from fastapi.encoders import jsonable_encoder
from models.log_request_dto import LogRequestDto
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config import channel

router = APIRouter()

@router.post('/ingest/')
async def ingestLog(log: LogRequestDto):
    try:
        log_dict = jsonable_encoder(log) 
        channel.basic_publish(
            exchange='',
            routing_key="logs_queue",
            body=json.dumps(log_dict)
        )
        return {"message": "Log ingested Succesfully"}
    except Exception:
        return JSONResponse(content={"error": "Failed to ingest log"}, status_code=500)



