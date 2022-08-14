import requests
import time
from config import API_KEY


def get_info():
    values = dict
    values["method"] = "getInfo"
    values["nonce"] = str(int(time.time()))

    header = {
        "key": API_KEY
    }

    response = requests.post(url="https://api.binance.com", headers=header, data=values)

    return response.json()


def main():
    print(get_info())

if __name__ == "__main__":
    main()