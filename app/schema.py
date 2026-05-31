from pydantic import BaseModel
from typing import Dict, Any

class LogSchema(BaseModel):
    module: str
    event: str
    timestamp: str
    data: Dict[str, Any]