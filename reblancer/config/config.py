from mimetypes import init
from pickletools import pyint
from py_compile import PycInvalidationMode
from tkinter.messagebox import NO
from typing import Optional, Dict, Any

from .load_config import load_config_file


class Config:

    def __init__(self, args: Dict[str, Any]) -> None:
        self.args = args
        self.config: Optional[Dict[str, Any]] = None

    def get_config(self):

        if self.config is None:
            self.config = self.load_config()

        return self.config

    @staticmethod
    def from_file(self):
        pass

    def load_config(self):
        config: Dict[str, Any] = load_config_file(self.args.get('config', []))

        self._parse_exchange(config)

        return config

    def get_auth(self, config: Dict[str, Any]) -> Dict[str, str]:
        return self.config['auth'] 
    
    def _parse_exchange(self, config: Dict[str, str]) -> None:
        exchange_config = config['exchange']
        name = exchange_config['name']
        auth = {
            'apiKey': exchange_config['key'],
            'secret': exchange_config['secret']
        }
        config['exchange_name'] = name
        config['auth'] = auth
