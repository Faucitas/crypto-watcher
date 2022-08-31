import os
import json

from typing import Any, Dict, Optional


def load_config_file(path: str) -> Dict[str, Any]:
    try:
        with open(path, 'r') as file:
            config = json.load(file)
    except FileNotFoundError as error:
        return print({'error': error})
    return config


