import json
import os
import ccxt
from pycoingecko import CoinGeckoAPI

from config.load_config import load_config_file
from config import Config


config = Config({'config': 'config.json'})

print(config.get_config())
# get Price Data

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
