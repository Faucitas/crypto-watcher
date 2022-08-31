import json
import os

import ccxt
from pycoingecko import CoinGeckoAPI

from config import Config
from utils import connect_to_exchange

current_dir = os.path.dirname(os.path.realpath(__file__))

config = Config({'config': os.path.join(current_dir,'config.json')})
config_obj = config.load_config()



# g et Price Data

exchange_auth = config_obj.get('auth')
exchange_name = config_obj.get('exchange_name')

exchange = connect_to_exchange(exchange_name, exchange_auth)
# markets = exchange.load_markets()'
# ticker = exchange.fetch_ticker('ETH/USD')



# Extract price

# Calculate balances in USD


# Re-balancing triggers


# print(f"Buy: {buy_eth_threshold}\nSell: {sell_eth_threshold}")



# text_content = ""
# formatted_gusd_percent = format_percent(gusd_percent)
# if gusd_percent < sell_eth_threshold:
#     text_content = f"Time to sell some ETH\nGUSD blance is now {formatted_gusd_percent} of your total balance."
#     send_text_message(text_content)
# elif gusd_percent > buy_eth_threshold:
#     text_content = f"Time to buy some ETH\nGUSD blance is now {formatted_gusd_percent} of your total balance."
#     send_text_message(text_content)
#
#
# print(text_content + formatted_gusd_percent)
