from typing import List, Optional
from pydantic import BaseModel, Field


class CatalogItem(BaseModel):
    entity_id: str = Field(..., description="Unique SHL assessment ID")

    name: str

    link: str

    description: Optional[str] = None

    duration: Optional[str] = None

    status: Optional[str] = None

    remote: Optional[str] = None

    adaptive: Optional[str] = None

    job_levels: List[str] = Field(default_factory=list)

    languages: List[str] = Field(default_factory=list)

    keys: List[str] = Field(default_factory=list)

    scraped_at: Optional[str] = None