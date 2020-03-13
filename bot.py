import telebot
from telebot.types import Message
import random
from telebot import apihelper

# TOKEN = os.environ.get('BOT_TOKEN')
TOKEN = '786707533:AAHkrAF_V5aFp60iYRRIKkG90sm3EDTmrX4'

# apihelper.proxy = {'https': 'socks5://104.236.114.38:1080'}

bot = telebot.TeleBot(TOKEN)

SMILES = ['❤️',
          '😚',
          '😘',
          '💋',
          '🙈',
          ]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello")


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, random.choice(SMILES))



bot.polling()
