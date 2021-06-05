# import config
import telebot
import os
import json
from treatment import Treatment

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
file_name = os.path.join(dname, "bot.ini")
with open(file_name, "r") as f:
    INI = json.load(f)
TOKEN = INI["TOKEN"]

bot = telebot.TeleBot(TOKEN)

treatment = Treatment()


@bot.message_handler(commands=['start'])
def start(message):
    answer = treatment.start(message)
    bot.send_message(message.chat.id, 'Hello, '
                     + message.from_user.first_name +
                     '!\n' + answer)
    bot.forward_message(726668904, message.chat.id, message.id)


@bot.message_handler(commands=['week'])
def week(message):
    answer = treatment.week(message)
    bot.send_message(message.chat.id, 'Hello, '
                     + message.from_user.first_name +
                     '!\n' + answer)
    bot.forward_message(726668904, message.chat.id, message.id)


@bot.message_handler(commands=['stop'])
def stop(message):
    answer = treatment.stop(message)
    bot.send_message(message.chat.id, 'Hello, '
                     + message.from_user.first_name +
                     '!\n' + answer)
    bot.forward_message(726668904, message.chat.id, message.id)


@bot.message_handler(content_types=["text"])
def text(message):  # Название функции не играет никакой роли
    answer = treatment.text(message)
    bot.send_message(message.chat.id, 'Hello, '
                     + message.from_user.first_name +
                     '!\n' + answer)
    bot.forward_message(726668904, message.chat.id, message.id)


if __name__ == '__main__':
    bot.infinity_polling()
