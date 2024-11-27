from sqlalchemy.orm import Session
from app.models import ChatHistory


def save_chat(db: Session, user_message: str, bot_response: str):
    chat = ChatHistory(user_message=user_message, bot_response=bot_response)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat
