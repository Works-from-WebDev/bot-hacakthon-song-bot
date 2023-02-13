import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import requests as req
import time
from keys import KEY
from lyrics import random_song
bot = telebot.TeleBot(KEY)
stringList = {'start': ['Play', 'Settings', 'Help'],
              'settings': ['Language', 'Theme', 'Back'],
              'language': ['English', 'Hebrew', 'Back'],
              'theme': ['Dark', 'Light', 'Back'],
              'help': ['How to play', 'About', 'Back']}


def handle_message(call):
    # Check if the message contains the correct song name
    if call.message.text.lower() == song_name.lower():
        bot.send_message(call.message.chat.id,
                         f'Winner: {call.message.from_user.id}')
        return True
    return False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(stringList['start'][0], callback_data='play'),
               InlineKeyboardButton(
                   stringList['start'][1], callback_data='settings'),
               InlineKeyboardButton(
                   stringList['start'][2], callback_data='help'),
               )
    bot.send_message(message.chat.id, 'Welcome to the game!',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'play')
def play_game(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, 'Welcome to the game!')
    data = random_song()
    song = data[2]
    actor = data[1]
    global song_name
    song_name = data[0]
    counter = 0

    # Send the first word
    bot.send_message(call.message.chat.id, song[counter])


@bot.callback_query_handler(func=lambda call: call.data == 'settings')
def setting(call):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(stringList['settings'][0], callback_data='language'),
               InlineKeyboardButton(
        stringList['settings'][1], callback_data='theme'),
        InlineKeyboardButton(
        stringList['settings'][2], callback_data='back'))
    bot.send_message(call.message.chat.id, 'Settings', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'language')
def language(call):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(stringList['language'][0], callback_data='english'),
               InlineKeyboardButton(
        stringList['language'][1], callback_data='hebrew'),
        InlineKeyboardButton(stringList['language'][2], callback_data='back'))
    bot.send_message(call.message.chat.id, 'Language', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'help')
def help(call):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(stringList['help'][0], callback_data='howtoplay'),
               InlineKeyboardButton(
        stringList['help'][1], callback_data='about'),
        InlineKeyboardButton(stringList['help'][2], callback_data='back'))
    bot.send_message(call.message.chat.id, 'Help', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'back')
def back(call):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(stringList['start'][0], callback_data='play'),
               InlineKeyboardButton(
        stringList['start'][1], callback_data='settings'),
        InlineKeyboardButton(
        stringList['start'][2], callback_data='help'),
    )
    bot.send_message(call.message.chat.id,
                     'Welcome to the game!', reply_markup=markup)


bot.infinity_polling()
