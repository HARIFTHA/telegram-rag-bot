import os
from rag.chunker import chunk_text
from rag.embedder import store_chunks

DOCS_PATH = "docs"

for filename in os.listdir(DOCS_PATH):
    if not filename.endswith((".txt", ".md")):
        continue

    file_path = os.path.join(DOCS_PATH, filename)

    with open(f"docs/{filename}", "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    chunks = chunk_text(text)
    store_chunks(chunks, source_name=filename)

    print(f"Ingested {filename} → {len(chunks)} chunks")

print("Ingestion completed!")