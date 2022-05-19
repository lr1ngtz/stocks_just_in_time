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
    assert StockSymbol.objects.count() == 0

    objs = StockSymbol.objects.all()
    expected_result = json_deserialize("stock_symbols__create.json")

    with patch.object(FinnhubAPI, "get_stocks", return_value=expected_result):
        create_or_update_stock_symbol()

        assert StockSymbol.objects.count() == 2
        assert objs[0].symbol == expected_result[0].get("symbol")
        assert objs[0].description == expected_result[0].get("description")


@pytest.mark.django_db
def test_create_or_update_stock_symbol__update():
    assert StockSymbol.objects.count() == 0

    objs = StockSymbol.objects.all()
    create_list = json_deserialize("stock_symbols__create.json")
    update_list = json_deserialize("stock_symbols__update.json")

    with patch.object(FinnhubAPI, "get_stocks", return_value=create_list):
        create_or_update_stock_symbol()
        assert StockSymbol.objects.count() == 2

    with patch.object(FinnhubAPI, "get_stocks", return_value=update_list):
        create_or_update_stock_symbol()
        assert StockSymbol.objects.count() == 2
        assert objs[0].description != create_list[0].get("description")
        assert objs[0].description == update_list[0].get("description")
