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

from keys import KEY

logging.basicConfig(
    format="[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

x = random_song()
print(x)


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    logger.info(f"> Start chat #{chat_id}")
    context.bot.send_message(chat_id=chat_id, text="💣 Welcome! 💣")

    j.run_once(callback_minute, 2, context={
        'chat_id': update.message.chat_id,
        'counter': 0,
    })


def callback_minute(context: telegram.ext.CallbackContext):
    d = context.job.context

    context.bot.send_message(chat_id=d['chat_id'], text=x[2][d['counter']])
    j.run_once(callback_minute, 2, context={
        'chat_id': d['chat_id'],
        'counter': d['counter'] + 1,
    })


def respond(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    response = text.replace("7", "💣")
    context.bot.send_message(chat_id=update.message.chat_id, text=response)


my_bot = Updater(token=KEY, use_context=True)
j = my_bot.job_queue

# if __name__ == '__main__':


my_bot.dispatcher.add_handler(CommandHandler("start", start))
my_bot.dispatcher.add_handler(MessageHandler(Filters.text, respond))

logger.info("* Start polling...")
my_bot.start_polling()  # Starts polling in a background thread.
my_bot.idle()  # Wait until Ctrl+C is pressed
logger.info("* Bye!")
