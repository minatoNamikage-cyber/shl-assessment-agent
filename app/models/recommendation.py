from pydantic import BaseModel, Field
from typing import List, Optional


class Recommendation(BaseModel):
    name: str = Field(..., description="Assessment name")
    url: str = Field(..., description="SHL catalog URL")
    reason: str = Field(..., description="Reason for recommendation")

    test_type: Optional[str] = None
    duration: Optional[str] = None
    languages: Optional[List[str]] = None