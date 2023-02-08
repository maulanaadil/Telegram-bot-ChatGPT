from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import os
from open_ai import get_response

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I am a Davinci-003 bot!")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="How can I help you today?")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = get_response(update.message.text)
    except Exception as exp:
        logger.info(f'{exp}')
    
    #response = f'```\npre-formatted fixed-width code block written in the Python programming language\n```'

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


if __name__ == '__main__':
    token = os.environ['BOT_TOKEN']
    application = ApplicationBuilder().token(token).build()
    

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    
    
    application.run_polling()