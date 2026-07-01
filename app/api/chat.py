from fastapi import APIRouter
from pydantic import BaseModel

from app.conversation.service import conversation_service

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    query: str


@router.post("")
async def chat(request: ChatRequest):

    return conversation_service.process(
        request.query
    )