# import config
import telebot
import json
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
file_name = os.path.join(dname, "bot.ini")
with open(file_name, "r") as f:
    INI = json.load(f)
TOKEN = INI["TOKEN"]


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)
    print(message.text)
if __name__ == '__main__':
     bot.infinity_polling()
