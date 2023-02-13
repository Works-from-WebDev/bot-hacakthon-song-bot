import logging
from lyrics import random_song
import telebot
from keys import API_KEY, KEY

bot = telebot.TeleBot(KEY)
logging.basicConfig(
    format="[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)
x = random_song()


def play(message):
    chat_id = message.chat.id
    logger.info(f"> Start chat #{chat_id}")
    bot.send_message(chat_id, "💣 Welcome!💣")
    bot.send_message(chat_id, x[2][0])
    bot.register_next_step_handler(message, callback_minute, 1)


def callback_minute(message, counter):
    chat_id = message.chat.id
    if counter >= len(x[2]):
        bot.send_message(chat_id, "You're lost")
    else:
        bot.send_message(chat_id, x[2][counter])
        bot.register_next_step_handler(message, callback_minute, counter + 1)


logger.info("* Start polling...")
bot.polling()  # Starts polling in a background thread.
logger.info("* Bye!")
