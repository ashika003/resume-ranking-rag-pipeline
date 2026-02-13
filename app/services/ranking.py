import base64
import numpy as np
from app.db import get_connection


def decode_embedding(blob: bytes) -> np.ndarray:
    raw = base64.b64decode(blob)
    return np.frombuffer(raw, dtype=np.float32)


def rank_resumes():
    conn = get_connection()
    job_row = conn.execute(
        "SELECT * FROM jobs ORDER BY id DESC LIMIT 1").fetchone()
    job_emb = decode_embedding(job_row["embedding"])

    ranked = []
    for r in conn.execute("SELECT * FROM resumes").fetchall():
        res_emb = decode_embedding(r["embedding"])
        score = np.dot(job_emb, res_emb) / \
            (np.linalg.norm(job_emb) * np.linalg.norm(res_emb))
        ranked.append({"name": r["name"], "score": float(score)})

    conn.close()
    return sorted(ranked, key=lambda x: x["score"], reverse=True)
