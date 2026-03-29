from sentence_transformers import SentenceTransformer
import sqlite3, json, numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def cosine_sim(a, b):
    a, b = np.array(a), np.array(b)

    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0 

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve(query, db_path="db/vectors.db", top_k=3):
    q_emb = model.encode(query).tolist()
    conn = sqlite3.connect(db_path)
    rows = conn.execute("SELECT source, text, embedding FROM chunks").fetchall()
    scored = [(cosine_sim(q_emb, json.loads(r[2])), r[0], r[1]) for r in rows]
    scored.sort(reverse=True)
    return scored[:top_k] 
