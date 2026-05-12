from pydantic import BaseModel, Field
from typing import Optional

class FocusSessionCreate(BaseModel):
    focus_level: int = Field(..., ge=1, le=5)
    duration_minutes: int = Field(..., gt=0)
    comment: str = Field(..., min_legth=5, max_length=300)
    category: Optional[str] = None
    