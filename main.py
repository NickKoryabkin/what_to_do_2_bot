import requests
import json
import telebot
from telebot import types

bot = telebot.TeleBot('5885698549:AAED14RzTpxF46UwYaGzNgfi5AORG_qRmeg')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Чем заняться?"))
    bot.send_message(message.chat.id, 'Данный бот при нажатие на кнопку "Чем заняться?" предложит вам то, чем вы можете занять свое время', reply_markup=markup)


@bot.message_handler()
def main(message):
    if message.text == "Чем заняться?":
        data = json.loads(requests.get('http://www.boredapi.com/api/activity/').text)
        bot.send_message(message.chat.id, data['activity'])


bot.polling(none_stop=True)
