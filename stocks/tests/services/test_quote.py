import json
from unittest.mock import patch

import pytest
from django.conf import settings
from stocks.exceptions import SymbolDoesNotExistException

from stocks.models import StockSymbol
from stocks.services.quote import create_quote
from finnhub.api import FinnhubAPI


def json_deserialize(file: str):

    with open(f"{settings.BASE_DIR}/stocks/tests/fixtures/{file}") as f:
        json_response = json.load(f)

    return json_response


@pytest.mark.django_db
def test_create_quote__symbol_does_not_exist():
    with pytest.raises(SymbolDoesNotExistException):
        create_quote("some_quote")


@pytest.mark.django_db
def test_create_quote__success():
    stock_symbol = json_deserialize("stock_symbol.json")
    stock_symbol = StockSymbol.objects.create(
        symbol=stock_symbol["symbol"],
        description=stock_symbol["description"],
        display_symbol=stock_symbol["displaySymbol"],
        figi=stock_symbol["figi"],
        isin=stock_symbol["isin"],
        mic=stock_symbol["mic"],
        share_class_figi=stock_symbol["shareClassFIGI"],
        symbol2=stock_symbol["symbol2"],
        type=stock_symbol["type"],
    )
    finnhub_response = json_deserialize("quote__success.json")

    with patch.object(FinnhubAPI, "get_quote", return_value=finnhub_response):
        quote = create_quote(stock_symbol.symbol)

        assert quote.current_price == finnhub_response["c"]
