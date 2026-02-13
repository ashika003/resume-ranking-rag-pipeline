from fastapi import FastAPI
from app.routers import info, upload, rank
from app.models import create_tables

# Create FastAPI app
app = FastAPI(
    title="Resume Ranking RAG Pipeline",
    description="API to upload resumes & job descriptions and rank candidates using embeddings",
    version="1.0.0"
)

# Create database tables automatically on startup


@app.on_event("startup")
def on_startup():
    create_tables()


# Include routers (register your endpoints)
app.include_router(info.router)
app.include_router(upload.router)
app.include_router(rank.router)
