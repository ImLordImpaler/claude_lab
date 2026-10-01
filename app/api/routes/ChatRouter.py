from fastapi import APIRouter
from app.api.schema.Chat import ChatResponse, ChatRequest

from app.services.chat import ChatService


router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    chat_service = ChatService()
    response = await chat_service.chat(request.message, request.conversation_id)
    return ChatResponse(response=response)