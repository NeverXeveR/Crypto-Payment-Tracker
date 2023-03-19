# Crypto Payment Checker

## Overview
This Python script is designed to monitor Bitcoin and Ethereum addresses for incoming transactions and send an email notification to a specified email address if a payment above a certain threshold is received. The script uses public APIs to retrieve information about the addresses and the cryptocurrency prices, and requires a Mailgun account to send the email notifications.

## Installation
To use this script, you need to have Python 3 installed on your computer. You also need to install the requests library by running the following command:

pip install requests

## Usage
1. Open the script in a code editor or text editor.
2. Replace API_KEY with your Mailgun API key.
3. Replace YOUR_EMAIL_ADDRESS with the email address you want to send the notifications from.
4. Replace RECIPIENT_EMAIL_ADDRESS with the email address you want to send the notifications to.
5. Replace BTC_THRESHOLD and ETH_THRESHOLD with the threshold amounts you want to set for Bitcoin and Ethereum payments respectively. These values are in satoshis and wei, respectively.
6. Add the Bitcoin and Ethereum addresses you want to monitor to the btc_addresses and eth_addresses lists.
7. Save the changes to the script.
8. Run the script by typing python scriptname.py in the terminal or command prompt.

# Dependencies
This script uses the following libraries:
- requests
- time

## API References
The script uses the following public APIs to retrieve information:

- Blockchain.info API for Bitcoin transactions: https://blockchain.info/api/blockchain_api
- BlockCypher API for Ethereum transactions: https://www.blockcypher.com/dev/ethereum/#introduction
- Coindesk API for Bitcoin price: https://www.coindesk.com/coindesk-api
- Coingecko API for Ethereum price: https://coingecko.com

## Credits
This script was created by "Run on the bank". Feel free to use, modify, and distribute this script as you wish.