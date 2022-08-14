import requests


def get_info():
    response = requests.get(url="http://yobitex.net/api/3/info")

    with open("info.txt", "w") as file:
        file.write(response.text)

    return response.text


def get_ticker(coin1, coin2):
    response = requests.get(
        url=f"http://yobitex.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1")

    with open("ticker.txt", "w") as file:
        file.write(response.text)

    return response.text


def get_depth(coin1, coin2, limit):
    response = requests.get(
        url=f"http://yobitex.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")
    with open("depth.txt", "w") as file:
        file.write(response.text)

    bids = response.json()[f"{coin1}_{coin2}"]["bids"]
    total_bids_amount = 0
    for item in bids:
        price = item[0]
        coin_count = item[1]
        total_bids_amount += price * coin_count

    return f"Total bids amount - {round(total_bids_amount, 2)}"


def trades(coin1, coin2, limit):
    response = requests.get(
        url=f"http://yobitex.net/api/3/trades/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")
    with open("trades.txt", "w") as file:
        file.write(response.text)

    total_trade_ask = 0
    total_trade_bid = 0

    for item in response.json()[f"{coin1}_{coin2}"]:
        if item["type"] == "ask":
            total_trade_ask += item["price"] * item["amount"]
        else:
            total_trade_bid += item["price"] * item["amount"]

    info = f"[-] TOTAL {coin1} SELL: {round(total_trade_ask, 2)} $ \n[+] TOTAL {coin1} BUY: {round(total_trade_bid, 2)} $"
    return info


def main():
    print(trades("btc", "usdt", 150))


if __name__ == "__main__":
    main()
