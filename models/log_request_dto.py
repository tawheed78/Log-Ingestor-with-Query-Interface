
from pydantic import BaseModel
from models.log_request_entity import LogRequestEntity

class LogRequestDto(BaseModel):
    level: str
    message: str
    resourceId: str
    timestamp: str
    traceId: str
    spanId: str
    commit: str
    metadata: dict

    def fromDtoToEntity(self) -> LogRequestEntity:
        return LogRequestEntity(self.level, self.message, self.resourceId, self.timestamp, self.traceId, self.spanId, self.commit, self.metadata)