import json

from django.conf import settings
from django.test import override_settings
import requests_mock

from finnhub.api import FinnhubAPI


def json_response(file: str):

    with open(f"{settings.BASE_DIR}/finnhub/tests/fixtures/{file}") as f:
        json_response = json.load(f)

    return json_response


@override_settings(FINNHUB_API_KEY=None)
def test_FinnhubConnection_get_stocks__api_key_absence():
    token = settings.FINNHUB_API_KEY
    expected_result = json_response("invalid_api.json")

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/stock/symbol?exchange=US&token={token}",
            json=expected_result,
        )
        result = FinnhubAPI(token)
        result = result.get_stocks()

        assert result == expected_result


def test_FinnhubConnection_get_stocks__success():
    token = settings.FINNHUB_API_KEY
    expected_result = json_response("stocks_success.json")

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/stock/symbol?exchange=US&token={token}",
            json=expected_result,
        )
        result = FinnhubAPI(token)
        result = result.get_stocks()

        assert result == expected_result


@override_settings(FINNHUB_API_KEY=None)
def test_FinnhubConnection_get_quote__api_key_absence():
    token = settings.FINNHUB_API_KEY
    expected_result = json_response("invalid_api.json")
    symbol = "some_symbol"

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={token}",
            json=expected_result,
        )
        result = FinnhubAPI(token)
        result = result.get_quote(symbol)

        assert result == expected_result


def test_FinnhubConnection_get_quote__empty_symbol():
    token = settings.FINNHUB_API_KEY
    expected_result = json_response("empty_or_null_symbol.json")

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/quote?symbol=&token={token}",
            json=expected_result,
        )
        result = FinnhubAPI(token)
        result = result.get_quote("")

        assert result == expected_result


def test_FinnhubConnection_get_quote__wrong_symbol():
    token = settings.FINNHUB_API_KEY
    expected_result = json_response("empty_or_null_symbol.json")
    symbol = "some_symbol"

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={token}",
            json=expected_result,
        )
        result = FinnhubAPI(token)
        result = result.get_quote(symbol)

        assert result == expected_result


def test_FinnhubConnection_get_quote__success():
    token = settings.FINNHUB_API_KEY
    expected_result = json_response("quote_success.json")
    symbol = "some_symbol"

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={token}",
            json=expected_result,
        )
        result = FinnhubAPI(token)
        result = result.get_quote(symbol)

        assert result == expected_result
