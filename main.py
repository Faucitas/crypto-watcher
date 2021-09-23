import dotenv
import os
from pycoingecko import CoinGeckoAPI
from twilio.rest import Client
dotenv.load_dotenv()

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_MESSAGE_SID = os.environ['TWILIO_MESSAGE_SID']
TWILIO_SENDING_NUMBER = os.environ['MY_PHONE_NUMBER']

TARGET_STABLE_PERCENT = 0.4
REBLANCE_THRESHOLD = 0.02



def send_text_message(message):
    # Send a message with the percentage
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        messaging_service_sid=TWILIO_MESSAGE_SID,
        body=message,
        to=TWILIO_SENDING_NUMBER
    )


def format_percent(percent):
    percent = round(percent * 100, 2)
    return f"{percent}%"


eth_bal = 0.33248320
gusd_bal = 697.26887289

cg = CoinGeckoAPI()

# get Price Data
eth_price_data = cg.get_price(ids='ethereum', vs_currencies='usd')
gusd_price_data = cg.get_price(ids='gemini-dollar', vs_currencies='usd')

# Extract price
eth_price = eth_price_data['ethereum']['usd']
gusd_price = gusd_price_data['gemini-dollar']['usd']

# Calculate balances in USD
eth_bal_in_usd = eth_price * eth_bal
gusd_bal_in_usd = gusd_price * gusd_bal
total_bal_in_usd = gusd_bal_in_usd + eth_bal_in_usd

# Re-balancing triggers
buy_eth_threshold = TARGET_STABLE_PERCENT + REBLANCE_THRESHOLD
sell_eth_threshold = TARGET_STABLE_PERCENT - REBLANCE_THRESHOLD

eth_percent = eth_bal_in_usd / total_bal_in_usd
gusd_percent = gusd_bal_in_usd / total_bal_in_usd

# print(f"Buy: {buy_eth_threshold}\nSell: {sell_eth_threshold}")
text_content = ""
formatted_gusd_percent = format_percent(gusd_percent)
if gusd_percent < sell_eth_threshold:
    text_content = f"Time to sell some ETH\nGUSD blance is now {formatted_gusd_percent} of your total balance."
    send_text_message(text_content)
elif gusd_percent > buy_eth_threshold:
    text_content = f"Time to buy some ETH\nGUSD blance is now {formatted_gusd_percent} of your total balance."
    send_text_message(text_content)


print(text_content + formatted_gusd_percent)
