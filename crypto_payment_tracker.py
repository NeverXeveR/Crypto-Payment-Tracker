import requests
import time

API_ENDPOINT_BTC = "https://blockchain.info/rawaddr/"
API_ENDPOINT_ETH = "https://api.blockcypher.com/v1/eth/main/addrs/"
BTC_THRESHOLD = 0  # in satoshis
ETH_THRESHOLD = 0  # in wei

btc_addresses = ['Add your BTC addresses here']
eth_addresses = ['Add your ETH addresses here']
frequency = 60  # in seconds
email_address = input("Enter your email address: ")
recipient_address = input("Enter recipient email address: ")

last_payments = {}


def check_btc_payment(address):
    url = API_ENDPOINT_BTC + address
    response = requests.get(url)
    data = response.json()
    if data["n_tx"] > 0:
        transaction = data["txs"][0]
        timestamp = transaction["time"]
        received = sum(output["value"] for output in transaction["out"] if output["addr"] == address)
        if received >= BTC_THRESHOLD:
            price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()["bpi"]["USD"]["rate_float"]
            amount_usd = received * price / 100000000
            if address not in last_payments or timestamp > last_payments[address] + frequency:
                message = f"Subject: Payment received\n\nPayment received on {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp))}\nAmount received: {received / 100000000:.8f} BTC\nCurrent Bitcoin price: {price:.2f} USD\nTotal amount received in USD: {amount_usd:.2f} USD"
                send_email(message)
                last_payments[address] = timestamp


def check_eth_payment(address):
    url = API_ENDPOINT_ETH + address + "/balance"
    response = requests.get(url)
    data = response.json()
    balance = int(data["balance"])
    if balance > 0:
        transactions_url = API_ENDPOINT_ETH + address + "/txs"
        transactions_response = requests.get(transactions_url)
        transactions_data = transactions_response.json()
        timestamp = transactions_data[0]["confirmed"]
        received = balance - int(transactions_data[0]["fees"])
        if received >= ETH_THRESHOLD:
            eth_price = \
                requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd").json()[
                    "ethereum"]["usd"]
            amount_usd = received * eth_price / 1000000000000000000
            if address not in last_payments or timestamp > last_payments[address] + frequency:
                message_f = f"Subject: Payment received\n\nPayment received on {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp))}\nAmount received: {received / 1000000000000000000:.8f} ETH\nCurrent Ethereum price: {eth_price:.2f} USD\nTotal amount received in USD: {amount_usd:.2f} USD"
                send_email(message_f)
                last_payments[address] = timestamp


def send_email(message):
    """
    Sends an email using Mailgun API. Create a free account at https://www.mailgun.com/ to get your API key and change the
    email addresses and the subject in the code below.
    """
    return requests.post(
        "https://api.mailgun.net/v3/sandboxa526358e0dcf481aa18a94d3bab0d64d.mailgun.org/messages",
        auth=("api", 'Add your API key here'),
        data={"from": 'Add the email address you want to send from here',
              "to": 'Add the email address you want to send to here',
              "subject": 'Add the subject here',
              "text": message
              })


while True:
    for address in btc_addresses:
        check_btc_payment(address)
    for address in eth_addresses:
        check_eth_payment(address)
    time.sleep(frequency)
