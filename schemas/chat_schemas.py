from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ChatCreate(BaseModel):
    message: str
    system_prompt: str = "You are a helpful assistant."


class ChatOut(BaseModel):
    id: int
    user_message: str
    ai_response: str
    created_at: datetime

    class Config:
        from_attributes = True
