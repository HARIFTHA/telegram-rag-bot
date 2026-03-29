import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3:mini"

def generate_answer(query, context_chunks):
    context = "\n\n".join([f"[{src}]: {txt}" for _, src, txt in context_chunks])

    prompt = f"""
You are a helpful assistant. Answer ONLY using the context below.
If not found, say: "I don't have information about that."

Context:
{context}

Question: {query}
Answer:
"""

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },timeout=30)
        print("⬅️ Response received")

        return response.json().get("response", "No response").strip()

    except Exception as e:
        print("❌ Ollama error:", e)
        return f"Error connecting to Ollama: {e}"