from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.chatbot import ask_chatbot
from app.schemas import ChatRequest, ChatResponse
from app.crud import save_chat

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, db: Session = Depends(get_db)):
    try:
        bot_response = ask_chatbot(request.message)
        save_chat(db, user_message=request.message, bot_response=bot_response)
        return ChatResponse(response=bot_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
