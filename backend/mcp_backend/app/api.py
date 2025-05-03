from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import openai
from app.database import get_db
from app.models import Conversation, Message
from app.schemas import ConversationCreate, Conversation as ConversationSchema
from app.schemas import MessageCreate, Message as MessageSchema
from app.schemas import ChatRequest, ChatResponse
from app.config import settings

router = APIRouter()

client = openai.OpenAI(api_key=settings.openai_api_key)

@router.post("/conversations/", response_model=ConversationSchema)
def create_conversation(conversation: ConversationCreate, db: Session = Depends(get_db)):
    db_conversation = Conversation(**conversation.model_dump())
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation

@router.get("/conversations/", response_model=List[ConversationSchema])
def read_conversations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    conversations = db.query(Conversation).offset(skip).limit(limit).all()
    return conversations

@router.get("/conversations/{conversation_id}", response_model=ConversationSchema)
def read_conversation(conversation_id: int, db: Session = Depends(get_db)):
    conversation = db.query(Conversation).filter(Conversation.id == conversation_id).first()
    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation

@router.post("/messages/", response_model=MessageSchema)
def create_message(message: MessageCreate, conversation_id: int, db: Session = Depends(get_db)):
    conversation = db.query(Conversation).filter(Conversation.id == conversation_id).first()
    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    db_message = Message(**message.model_dump(), conversation_id=conversation_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@router.post("/chat/", response_model=ChatResponse)
async def chat(request: ChatRequest, db: Session = Depends(get_db)):
    if request.conversation_id is None:
        conversation = Conversation(title="New Conversation")
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
    else:
        conversation = db.query(Conversation).filter(Conversation.id == request.conversation_id).first()
        if conversation is None:
            raise HTTPException(status_code=404, detail="Conversation not found")
    
    user_message = Message(
        conversation_id=conversation.id,
        role="user",
        content=request.message
    )
    db.add(user_message)
    db.commit()
    
    messages = db.query(Message).filter(Message.conversation_id == conversation.id).all()
    
    openai_messages = [{"role": msg.role, "content": msg.content} for msg in messages]
    
    system_message = {
        "role": "system", 
        "content": "You are an AI assistant for the 'trast' project. Your purpose is to help new team members understand the project specifications and answer questions about the project. Provide detailed and accurate information based on the project's documentation."
    }
    openai_messages.insert(0, system_message)
    
    try:
        response = client.chat.completions.create(
            model=settings.model_name,
            messages=openai_messages
        )
        
        assistant_response = response.choices[0].message.content
        
        assistant_message = Message(
            conversation_id=conversation.id,
            role="assistant",
            content=assistant_response
        )
        db.add(assistant_message)
        db.commit()
        
        return {"conversation_id": conversation.id, "message": assistant_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calling OpenAI API: {str(e)}")
