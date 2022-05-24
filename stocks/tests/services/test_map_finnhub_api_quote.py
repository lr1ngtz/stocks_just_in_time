import json
from datetime import datetime

import pytest
from django.conf import settings

from stocks.exceptions import UnexpectedQuoteInfoException
from stocks.services.map_finnhub_api_quote import map_finnhub_api_quote


def json_deserialize(file: str):

    with open(f"{settings.BASE_DIR}/stocks/tests/fixtures/{file}") as f:
        json_response = json.load(f)

    return json_response


def test_map_finnhub_api_quote__fail():
    quote_info = json_deserialize("quote__fail.json")
    stock_symbol = None

    with pytest.raises(UnexpectedQuoteInfoException):
        map_finnhub_api_quote(quote_info, stock_symbol)


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
