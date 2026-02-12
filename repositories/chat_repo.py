from model import ChatHistory
from sqlalchemy.orm import Session


class ChatRepo:
    def __init__(self, db: Session):
        self.db = db

    def save_chat(self, user_message: str, ai_response: str):
        chat = ChatHistory(user_message=user_message, ai_response=ai_response)
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)
        return chat

    def get_all_chats(self):
        return self.db.query(ChatHistory).order_by(ChatHistory.created_at.desc()).all()
