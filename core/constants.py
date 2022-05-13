import os

from dotenv import load_dotenv

WRONG_SYMBOL_OUTPUT = {
    "c": 0,
    "d": None,
    "dp": None,
    "h": 0,
    "l": 0,
    "o": 0,
    "pc": 0,
    "t": 0,
}

load_dotenv()

API_KEY = os.environ.get("API_KEY")
