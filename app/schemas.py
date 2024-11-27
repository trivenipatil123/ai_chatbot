from pydantic import BaseModel
from datetime import datetime


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


class ChatHistory(BaseModel):
    id: int
    user_message: str
    bot_response: str
    timestamp: datetime

    class Config:
        orm_mode = True
