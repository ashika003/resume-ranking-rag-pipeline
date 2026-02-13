from sentence_transformers import SentenceTransformer
import numpy as np
import base64

model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text: str) -> bytes:
    emb = model.encode(text)
    raw = np.array(emb, dtype=np.float32).tobytes()
    return base64.b64encode(raw)
