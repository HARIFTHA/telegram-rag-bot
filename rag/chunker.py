def chunk_text(text, chunk_size=300, overlap=50):
    words = text.split()
    chunks = []
    step = chunk_size - overlap

    for i in range(0, len(words), step):
        chunk = words[i:i + chunk_size]
        if len(chunk) > 20:
            chunks.append(" ".join(chunk))

    return chunks
