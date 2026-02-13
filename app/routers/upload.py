from fastapi import APIRouter, UploadFile, File
from app.services.text_extraction import extract_text
from app.services.embeddings import generate_embedding
from app.db import get_connection

router = APIRouter(prefix="/upload")


@router.post("/resumes")
async def upload_resumes(files: list[UploadFile] = File(...)):
    conn = get_connection()
    for f in files:
        # Extract content
        text = extract_text(await f.read(), f.filename)
        # Generate embedding
        emb = generate_embedding(text)
        # Insert into DB
        conn.execute(
            "INSERT INTO resumes (name, content, embedding) VALUES (?, ?, ?)",
            (f.filename, text, emb)
        )
    conn.commit()
    conn.close()
    return {"message": "Resumes uploaded successfully"}


@router.post("/job")
async def upload_job(file: UploadFile = File(...)):
    conn = get_connection()
    text = extract_text(await file.read(), file.filename)
    emb = generate_embedding(text)
    conn.execute(
        "INSERT INTO jobs (title, content, embedding) VALUES (?, ?, ?)",
        (file.filename, text, emb)
    )
    conn.commit()
    conn.close()
    return {"message": "Job uploaded successfully"}
