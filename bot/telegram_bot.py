from telegram import Update
from telegram.ext import ContextTypes
from rag.retriever import retrieve
from rag.llm import generate_answer

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)

    print("Received query:", query)

    if not query:
        await update.message.reply_text("Usage: /ask <your question>")
        return

    print("Retrieving chunks...")
    chunks = retrieve(query, top_k=3)

    print("Generating answer...")
    answer = generate_answer(query, chunks)

    print("Answer generated:", answer)

    reply = f"Answer:\n{answer}\n\n Sources:\n"

    for score, src, text in chunks:
        reply += f"- {src}: {text[:100]}...\n"

    print("Sending reply to Telegram...")
    await update.message.reply_text(reply)



async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/ask <question> — Ask from knowledge base\n"
        "/help — Show commands"
    )
