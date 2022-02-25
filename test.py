from tinydb import TinyDB, where, Query
from datetime import datetime as dt
from pycoingecko import CoinGeckoAPI

db = TinyDB('db.json')
cg = CoinGeckoAPI()


class Config:
    def __init__(self):
        self.table = self.set_table('config')
        self.name = None
        self.value = None

    def set_table(self, table_name):
        table = db.table(table_name)
        self.table = table
        return self.table


class Asset:
    TABLE_NAME = 'assets'
    def __init__(self, id):
        self.id = id
        self.table = self.set_table('cg_id')
        self.symbol = self.get('symbol')
        self.name = self.get('name')
        self.balance = self.get('balance')
        self.updated_at = self.get('updated_at')

    def set_table(self, index):
        table = db.table(self.TABLE_NAME).search(where(index) == self.id)[0]
        self.table = table
        return self.table

    def get(self, key):
        return self.table[key]



