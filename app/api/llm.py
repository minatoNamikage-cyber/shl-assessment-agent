from fastapi import APIRouter
from pydantic import BaseModel

from app.llm.llm import llm_service

router = APIRouter(
    prefix="/llm",
    tags=["LLM"]
)


class LLMRequest(BaseModel):
    query: str


@router.post("/test")
async def test_llm(request: LLMRequest):

    result = llm_service.analyze(request.query)

    return result