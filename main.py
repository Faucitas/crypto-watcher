from pycoingecko import CoinGeckoAPI

TARGET_STABLE_PERCENT = 0.4
REBLANCE_THRESHOLD = 0.02


def format_percent(percent):
    percent = round(percent * 100, 2)
    return f"{percent}%"


eth_bal = 0.33952907
gusd_bal = 655.19363511

cg = CoinGeckoAPI()

eth_price_data= cg.get_price(ids='ethereum', vs_currencies='usd')
gusd_price_data = cg.get_price(ids='gemini-dollar', vs_currencies='usd')

eth_price = eth_price_data['ethereum']['usd']
gusd_price = gusd_price_data['gemini-dollar']['usd']

eth_bal_in_usd = eth_price * eth_bal
gusd_bal_in_usd = gusd_price * gusd_bal
total_bal_in_usd = gusd_bal_in_usd + eth_bal_in_usd

buy_eth_threshold = TARGET_STABLE_PERCENT + REBLANCE_THRESHOLD
sell_eth_threshold = TARGET_STABLE_PERCENT - REBLANCE_THRESHOLD


eth_percent = eth_bal_in_usd / total_bal_in_usd
gusd_percent = gusd_bal_in_usd / total_bal_in_usd

# print(f"Buy: {buy_eth_threshold}\nSell: {sell_eth_threshold}")

if gusd_percent < sell_eth_threshold:
    print("Time to sell some ETH")
elif gusd_percent > buy_eth_threshold:
    print("Time to buy some ETH")

print(format_percent(gusd_percent))