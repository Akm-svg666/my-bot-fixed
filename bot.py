import os, threading
from flask import Flask
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
TOKEN = os.getenv("BOT_TOKEN")
async def start(update, context):
    await update.message.reply_text("هلا! دزلي ملف")
async def handle_file(update, context):
    await update.message.reply_text("وصل!")
def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    app.run_polling()
threading.Thread(target=run_bot, daemon=True).start()
flask_app = Flask(__name__)
@flask_app.route("/")
def home(): return "Bot is running"
if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
