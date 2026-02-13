from fastapi import APIRouter
from app.services.ranking import rank_resumes
from app.schemas import RankResponse

router = APIRouter(prefix="/rank")


@router.get("/", response_model=RankResponse)
def rank():
    results = rank_resumes()
    return {"ranked": results}
