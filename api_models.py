from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    message: str
    building: str
    chat_history: List[dict] = []

class ChatResponse(BaseModel):
    message: str
    building: str
    chat_history: List[dict]

class BuildingResponse(BaseModel):
    buildings: List[str]

class BuildingInfoResponse(BaseModel):
    building_number: str
    info: str
