from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

async def greet_new_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"Welcome {member.first_name}!")

async def delete_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "http" in update.message.text:
        await update.message.delete()
        await update.message.reply_text("Links are not allowed!")

if __name__ == '__main__':
    application = "8598832324:AAFHhCQVsWXDRCZUg3Ps1pdDtcLWTKlwuh4" ApplicationBuilder().token('YOUR_BOT_TOKEN_HERE').build()

    new_member_handler = MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, greet_new_members)
    link_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), delete_links)

    application.add_handler(new_member_handler)
    application.add_handler(link_handler)

    application.run_polling()
