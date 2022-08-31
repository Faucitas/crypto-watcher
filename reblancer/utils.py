from typing import Dict, Any

import ccxt

def format_percent(percent):
    percent = round(percent * 100, 2)
    return f"{percent}%"


def connect_to_exchange(exchange_name: str, exchange_auth: Dict[str, str]):
    """
    Connects to specified crypto and returns CCXT exchange object
    :param exchange_name: ccxt exchange id
    :param exchange_auth: Dictionary containing the exchange API key and secret
    :return: CCXT exchange object
    """
    exchange_class = getattr(ccxt, exchange_name)
    return exchange_class(exchange_auth)