from sentence_transformers import SentenceTransformer
import sqlite3, json, os

model = SentenceTransformer("all-MiniLM-L6-v2")

def store_chunks(chunks, source_name, db_path="db/vectors.db"):
   
    os.makedirs("db", exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chunks 
        (id INTEGER PRIMARY KEY, source TEXT, text TEXT, embedding TEXT)
    """)

    for chunk in chunks:
        emb = model.encode(chunk).tolist()
        cursor.execute(
            "INSERT INTO chunks (source, text, embedding) VALUES (?, ?, ?)",
            (source_name, chunk, json.dumps(emb))
        )

    conn.commit()
    conn.close()