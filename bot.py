import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import requests as req
from keys import KEY
bot = telebot.TeleBot(KEY)
stringList = {'start': ['Play', 'Settings', 'Help'],
              'settings': ['Language', 'Theme', 'Back'],
              'language': ['English', 'Hebrew', 'Back'],
              'theme': ['Dark', 'Light', 'Back'],
              'help': ['How to play', 'About', 'Back']
              }

x§


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


@bot.callback_query_handler(func=lambda call: True)
def process_callback(call):
    if call.data == 'play':

        bot.send_message(call.message.chat.id, 'Play')

    elif call.data == 'settings':

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(stringList['settings'][0], callback_data='language'),
                   InlineKeyboardButton(
                       stringList['settings'][1], callback_data='theme'),
                   InlineKeyboardButton(
                       stringList['settings'][2], callback_data='back'))
        bot.send_message(call.message.chat.id, 'Settings', reply_markup=markup)
    elif call.data == 'language':
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(stringList['language'][0], callback_data='english'),
                   InlineKeyboardButton(
                       stringList['language'][1], callback_data='hebrew'),
                   InlineKeyboardButton(stringList['language'][2], callback_data='back'))
        bot.send_message(call.message.chat.id, 'Language', reply_markup=markup)

    elif call.data == 'help':

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(stringList['help'][0], callback_data='howtoplay'),
                   InlineKeyboardButton(
                       stringList['help'][1], callback_data='about'),
                   InlineKeyboardButton(stringList['help'][2], callback_data='back'))
        bot.send_message(call.message.chat.id, 'Help', reply_markup=markup)
    elif call.data == 'back':
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(stringList['start'][0], callback_data='play'),
                   InlineKeyboardButton(
                       stringList['start'][1], callback_data='settings'),
                   InlineKeyboardButton(
                       stringList['start'][2], callback_data='help'),
                   )
        bot.send_message(call.message.chat.id,
                         'Welcome to the game!', reply_markup=markup)


bot.polling()
