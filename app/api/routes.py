from fastapi import APIRouter
from app.schemas.request_response import MatchRequest, MatchResponse
from app.services.matcher import analyze_match

router = APIRouter()

@router.post("/analyze", response_model=MatchResponse)
def analyze_resume_jd(data: MatchRequest):
    result = analyze_match(data.resume_text, data.jd_text)
    return result
