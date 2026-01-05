from pydantic import BaseModel
from typing import List

class MatchRequest(BaseModel):
    resume_text: str
    jd_text: str

class MatchResponse(BaseModel):
    match_score: float
    matched_keywords: List[str]
    missing_keywords: List[str]
