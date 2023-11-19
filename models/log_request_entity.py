
from pydantic import BaseModel
from datetime import datetime


class LogRequestEntity:
    def __init__(self, level, message, resourceId, timestamp, traceId, spanId, commit, metadata):
        id: int = None
        level: str
        message: str
        resourceId: str
        timestamp: str
        traceId: str
        spanId: str
        commit: str
        metadata: dict