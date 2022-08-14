import requests
from bs4 import BeautifulSoup


class Currency_Dollar:
    DOLLAR_RUB = 'https://www.cbr.ru/currency_base/daily/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    current_converted_price = 0
    difference = 5

    def __init__(self):
        self.current_converted_price = float(
            self.get_currency_price().replace(",", "."))

    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb",
                                        "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            print("Курс сильно вырос, может пора что-то делать?")

        elif currency <= self.current_converted_price - self.difference:
            print("Курс сильно упал, может пора что-то делать?")

        print("Сейчас курс: 1 доллар = " + str(currency))


class Currency_Euro:
    EURO_RUB = "https://www.google.com/search?q=E%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=ALiCzsYPTdP2B5sOVT8O-2ug-gSPIKLPyw%3A1651728535422&ei=l2BzYsGpGYuRrwTclqH4Dg&ved=0ahUKEwiB0fmk0Mf3AhWLyIsKHVxLCO8Q4dUDCA4&uact=5&oq=E%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEIMBEEMyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEEMyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAo6BggAEAcQHjoECAAQDToICAAQDRAFEB46CggAEAcQChAeECpKBAhBGABKBAhGGABQAFj9DWCFFWgBcAF4AIABjgGIAc8DkgEDMy4ymAEAoAEBwAEB&sclient=gws-wiz"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    current_converted_price = 0
    difference = 5

    def __init__(self):
        self.current_converted_price = float(
            self.get_currency_price().replace(",", "."))

    def get_currency_price(self):
        full_page = requests.get(self.EURO_RUB, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb",
                                        "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            print("Курс сильно вырос, может пора что-то делать?")

        elif currency <= self.current_converted_price - self.difference:
            print("Курс сильно упал, может пора что-то делать?")

        print("Сейчас курс: 1 евро = " + str(currency))


dollar = Currency_Dollar()
dollar.check_currency()

euro = Currency_Euro()
euro.check_currency()