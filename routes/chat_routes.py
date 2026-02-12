from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from repositories.chat_repo import ChatRepo
from schemas.chat_schemas import ChatCreate, ChatOut
from utils.ai_response_utils import get_completion
from typing import List

router = APIRouter()


@router.post("/chat", response_model=ChatOut)
def chat(request: ChatCreate, db: Session = Depends(get_db)):
    """Send a message to AI and save the conversation to history."""
    try:
        ai_response = get_completion(request.message, request.system_prompt)
        chat_repo = ChatRepo(db)
        chat = chat_repo.save_chat(request.message, ai_response)
        return chat
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/chat/history", response_model=List[ChatOut])
def get_chat_history(db: Session = Depends(get_db)):
    """Get all chat history, newest first."""
    chat_repo = ChatRepo(db)
    return chat_repo.get_all_chats()
