from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()


# eth_price_data = cg.get_price(ids='ethereum', vs_currencies='usd')
eth_price_data = cg.get_price(ids='ethereum', vs_currencies='usd, btc', include_market_cap=True)
# history = cg.g

price = eth_price_data['ethereum']['usd']