import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler
from bot.telegram_bot import ask, help_cmd

print("Starting bot...")

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

print("Token loaded:", TOKEN)

app = ApplicationBuilder().token(TOKEN).build()

print("App built")

app.add_handler(CommandHandler("ask", ask))
app.add_handler(CommandHandler("help", help_cmd))

print("Handlers added")

app.run_polling()

print("Bot is running...")
