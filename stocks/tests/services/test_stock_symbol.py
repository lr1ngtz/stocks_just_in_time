import json
from unittest.mock import patch

import pytest
from django.conf import settings

from stocks.models import StockSymbol
from stocks.services.stock_symbol import create_or_update_stock_symbol
from finnhub.api import FinnhubAPI


def json_deserialize(file: str):

    with open(f"{settings.BASE_DIR}/stocks/tests/fixtures/{file}") as f:
        json_response = json.load(f)

    return json_response


@pytest.mark.django_db
def test_create_or_update_stock_symbol__create():
    before_count = StockSymbol.objects.count()

    finnhub_response = json_deserialize("stock_symbols__create.json")

    with patch.object(FinnhubAPI, "get_stocks", return_value=finnhub_response):
        create_or_update_stock_symbol()
        after_count = StockSymbol.objects.count()

        assert before_count + 2 == after_count


@pytest.mark.django_db
def test_create_or_update_stock_symbol__update():
    before_count = StockSymbol.objects.count()

    finnhub_response = json_deserialize("stock_symbols__create.json")
    update_list = json_deserialize("stock_symbols__update.json")

    with patch.object(FinnhubAPI, "get_stocks", return_value=finnhub_response):
        create_or_update_stock_symbol()
        after_count = StockSymbol.objects.count()

        assert before_count + 2 == after_count
        create_or_update_stock_symbol()

    with patch.object(FinnhubAPI, "get_stocks", return_value=update_list):
        create_or_update_stock_symbol()

        stock_symbols_descriptions = list(
            StockSymbol.objects.values_list("description", flat=True)
        )
        for stock in update_list:
            assert stock["description"] in stock_symbols_descriptions

        assert before_count + 2 == after_count
