from unittest.mock import patch

import pytest
from stocks.models import Quote

from stocks.services.quote import create_quote
from finnhub.api import FinnhubAPI
from stocks.tests.utils import json_deserialize


@pytest.mark.django_db
def test_create_quote__success(apple_stock):
    finnhub_response = json_deserialize("quote__success.json")

    with patch.object(FinnhubAPI, "get_quote", return_value=finnhub_response):
        create_quote(apple_stock.symbol)

        assert Quote.objects.count() == 1
