from pydantic import BaseModel
from typing import List, Optional

from app.models.recommendation import Recommendation


class ChatResponse(BaseModel):
    reply: str

    recommendations: Optional[List[Recommendation]] = None

    end_of_conversation: bool