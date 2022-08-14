from datetime import datetime

import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

now = datetime.now()


class CurrencyParse:
    def __init__(self, data):
        self.data = data
        self.date_today = now.strftime("%d/%m/%Y %H:%M:%S")

    def get_dollar(self):
        return f'Курс доллара на {self.date_today}: {self.data["Valute"]["USD"]["Value"]} ₽'

    def get_euro(self):
        return f'Курс евро на {self.date_today}: {self.data["Valute"]["EUR"]["Value"]} ₽'


value = CurrencyParse(data)

print(value.get_euro())
print(value.get_dollar())
