import logging

from lyrics import random_song
import telegram
from telegram import Update
from telegram.ext import (
    CommandHandler,
    CallbackContext,
    MessageHandler,
    Filters,
    Updater,
)

import bot_settings

logging.basicConfig(
    format="[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    if context.user_data.get("song"):
        return
    song = random_song("BOTH")
    context.user_data["song"]=song
    logger.info(f"> Start chat #{chat_id},song ={song[0]}")
    context.bot.send_message(chat_id=chat_id, text="guess the song")

    j.run_once(callback_minute, 2, context={
        'chat_id': update.message.chat_id,
        'counter': 0,
        "song": song
    })


def callback_minute(context: telegram.ext.CallbackContext):
    d = context.job.context
    song = d["song"]
    context.bot.send_message(chat_id=d['chat_id'], text=song[2][d['counter']])
    j.run_once(callback_minute, 2, context={
        'chat_id': d['chat_id'],
        'counter': d['counter'] + 1,
        "song": song
    })


def respond(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    response = text.replace("7", "💣")
    context.bot.send_message(chat_id=update.message.chat_id, text=response)


my_bot = Updater(token=bot_settings.BOT_TOKEN, use_context=True)
j = my_bot.job_queue

# if __name__ == '__main__':


my_bot.dispatcher.add_handler(CommandHandler("start", start))
my_bot.dispatcher.add_handler(MessageHandler(Filters.text, respond))

logger.info("* Start polling...")
my_bot.start_polling()  # Starts polling in a background thread.
my_bot.idle()  # Wait until Ctrl+C is pressed
logger.info("* Bye!")
