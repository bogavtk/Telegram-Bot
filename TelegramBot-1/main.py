from datetime import datetime

import requests
import telebot

from auth_data import token

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

now = datetime.now()


class CurrencyParse:
    def __init__(self, data):
        self.data = data
        self.date_today = now.strftime("%d/%m/%Y %H:%M")

    def get_dollar(self):
        return f'Dollar currency on {self.date_today}: {self.data["Valute"]["USD"]["Value"]}₽'

    def get_euro(self):
        return f'Euro currency on {self.date_today}: {self.data["Valute"]["EUR"]["Value"]}₽'

value = CurrencyParse(data)


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id,
                         "Hi! U're on bot's main page. What do u want? ")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text == "dollar":
            try:
                bot.send_message(message.chat.id, value.get_dollar())
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Damn...Sorry, not today..."
                )
        elif message.text == "euro":
            try:
                bot.send_message(message.chat.id, value.get_euro())
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Damn...Sorry, not today..."
                )
        else:
            bot.send_message(message.chat.id,
                             "Oh...Maybe u entered wrong currency")

    bot.polling()  # Checking new messages


if __name__ == "__main__":
    telegram_bot(token)
