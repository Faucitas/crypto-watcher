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
        config: Dict[str, Any] = load_config_file(self.args.get('config', ''))

        return config
