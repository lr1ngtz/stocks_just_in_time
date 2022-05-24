from datetime import datetime

from stocks.services.map_finnhub_api_quote import map_finnhub_api_quote
from stocks.tests.utils import json_deserialize


def test_map_finnhub_api_quote__success():
    quote_info = json_deserialize("quote__success.json")
    stock_symbol = None
    expected_result = {
        "current_price": 143.11,
        "change": 5.52,
        "percent_change": 4.0119,
        "high_price_of_the_day": 143.26,
        "low_price_of_the_day": 137.8601,
        "open_price_of_the_day": 137.79,
        "previous_close_price": 137.59,
        "timestamp": datetime.fromtimestamp(1653336003),
    }
    result = map_finnhub_api_quote(quote_info, stock_symbol)

    assert result["current_price"] == expected_result["current_price"]
    assert result["timestamp"] == expected_result["timestamp"]
