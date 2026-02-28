import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bot is working!')

if __name__ == '__main__':
    TOKEN = "8598832324:AAFHhCQVsWXDRCZUg3Ps1pdDtcLWTKlwuh4"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    print("Bot is running...")
    application.run_polling()
