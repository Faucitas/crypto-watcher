import os
import json

from typing import Dict, Optional


def load_config_file(path: str) -> Dict:
    try:
        with open(path, 'r') as file:
            config = json.load(file)
    except FileNotFoundError as error:
        print({'error': error})
    return config


