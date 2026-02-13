from pydantic import BaseModel
from typing import List


class UploadResponse(BaseModel):
    message: str


class RankItem(BaseModel):
    name: str
    score: float


class RankResponse(BaseModel):
    ranked: List[RankItem]
