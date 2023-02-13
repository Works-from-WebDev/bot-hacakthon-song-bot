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

# settings
interval = 5
times = 30

logging.basicConfig(
    format="[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


class State:
    def __init__(self, chat_id, name, artist, lyrics):
        self.chat_id = chat_id
        self.name = name
        self.artist = artist
        self.lyrics = lyrics
        self.running = True
        self.counter = 0

    def __repr__(self):
        return f"Song(name={self.name!r}, chat_id={self.chat_id})"


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    if context.user_data.get("song") and context.user_data["song"].running:
        return

    name, artist, lyrics = random_song("BOTH")
    song = State(chat_id, name, artist, lyrics)
    context.user_data["song"] = song
    logger.info(f"> Start chat #{chat_id},song={song}")
    context.bot.send_message(
        chat_id=chat_id, text=f"Hi welcome to the Guessing The Song game!!!"
    )

    j.run_once(callback_minute, 1.5, context=song)


def callback_minute(context: telegram.ext.CallbackContext):
    song: State = context.job.context
    if not song.running:
        return
    if song.counter > times:
        context.bot.send_message(chat_id=song.chat_id, text="sorry you lost")
        song.running = False
        return
    context.bot.send_message(chat_id=song.chat_id, text=song.lyrics[song.counter])
    song.counter += 1
    j.run_once(callback_minute, interval, context=song)


def guess(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    song = context.user_data.get("song")
    if not song:
        return
    if not song.running:
        return

    success = text.lower() == song.name.lower()
    msg = (
        f"You got it!!! the name of the song is: {song.name} by the artist: {song.artist}"
        if success
        else f"{text} is not the song's name"
    )
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)
    logger.info(f"= Got on chat #{chat_id}: {text!r} {success=}")
    if success:
        song.running = False


my_bot = Updater(token=bot_settings.BOT_TOKEN, use_context=True)
j = my_bot.job_queue

# if __name__ == '__main__':


my_bot.dispatcher.add_handler(CommandHandler("start", start))
my_bot.dispatcher.add_handler(MessageHandler(Filters.text, guess))

logger.info("* Start polling...")
my_bot.start_polling()  # Starts polling in a background thread.
my_bot.idle()  # Wait until Ctrl+C is pressed
logger.info("* Bye!")