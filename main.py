from telegram.ext import Application
from bot import register
from config import BOT_TOKEN

app = Application.builder().token(BOT_TOKEN).build()

register(app)

app.run_polling()
