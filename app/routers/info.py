from fastapi import APIRouter

router = APIRouter(prefix="/info")


@router.get("/")
def info():
    return {"message": "Resume Ranking RAG API is running"}
