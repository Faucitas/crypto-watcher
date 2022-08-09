import json
import ccxt
from pycoingecko import CoinGeckoAPI


TARGET_STABLE_PERCENT = 0.40
REBALANCE_THRESHOLD = 0.02


eth_bal = 0.28926629
gusd_bal = 912.13888679


cg = CoinGeckoAPI()

def format_percent(percent):
    percent = round(percent * 100, 2)
    return f"{percent}%"



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
