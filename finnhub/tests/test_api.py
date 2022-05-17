import json

from django.conf import settings
import requests_mock
import pytest

from finnhub.api import FinnhubAPI
from finnhub.exceptions import FinnhubAPIException


def json_response(file: str):

    with open(f"{settings.BASE_DIR}/finnhub/tests/fixtures/{file}") as f:
        json_response = json.load(f)

    return json_response


def test_FinnhubConnection_get_stocks__api_key_absence():
    token = None
    expected_result = json_response("invalid_api.json")

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/stock/symbol?exchange=US&token={token}",
            json=expected_result,
            status_code=401,
        )
        with pytest.raises(FinnhubAPIException, match="Invalid API key"):
            result = FinnhubAPI(token)
            result.get_stocks()


def test_FinnhubConnection_get_stocks__exceed_limit():
    token = settings.FINNHUB_API_KEY
    expected_result = json_response("429.json")

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/stock/symbol?exchange=US&token={token}",
            json=expected_result,
            status_code=429,
        )
        with pytest.raises(FinnhubAPIException, match=""):
            result = FinnhubAPI(token)
            result.get_stocks()


def test_FinnhubConnection_get_stocks__internal_error():
    token = settings.FINNHUB_API_KEY
    expected_result = json_response("500.json")

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/stock/symbol?exchange=US&token={token}",
            json=expected_result,
            status_code=500,
        )
        with pytest.raises(FinnhubAPIException, match=""):
            result = FinnhubAPI(token)
            result.get_stocks()


def test_FinnhubConnection_get_stocks__success():
    token = settings.FINNHUB_API_KEY
    expected_result = json_response("stocks_success.json")

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/stock/symbol?exchange=US&token={token}",
            json=expected_result,
            status_code=200,
        )
        result = FinnhubAPI(token)
        result = result.get_stocks()

        assert result == expected_result


def test_FinnhubConnection_get_quote__api_key_absence():
    token = None
    expected_result = json_response("invalid_api.json")
    symbol = "some_symbol"

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={token}",
            json=expected_result,
            status_code=401,
        )
        with pytest.raises(FinnhubAPIException, match="Invalid API key"):
            result = FinnhubAPI(token)
            result.get_quote(symbol)


def test_FinnhubConnection_get_quote__exceed_limit():
    token = None
    expected_result = json_response("429.json")
    symbol = "some_symbol"

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={token}",
            json=expected_result,
            status_code=429,
        )
        with pytest.raises(FinnhubAPIException, match=""):
            result = FinnhubAPI(token)
            result.get_quote(symbol)


def test_FinnhubConnection_get_quote__internal_error():
    token = None
    expected_result = json_response("500.json")
    symbol = "some_symbol"

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={token}",
            json=expected_result,
            status_code=500,
        )
        with pytest.raises(FinnhubAPIException, match=""):
            result = FinnhubAPI(token)
            result.get_quote(symbol)


def test_FinnhubConnection_get_quote__empty_symbol():
    token = settings.FINNHUB_API_KEY
    expected_result = json_response("empty_or_null_symbol.json")

    with requests_mock.Mocker() as m:
        m.get(
            f"https://finnhub.io/api/v1/quote?symbol=&token={token}",
            json=expected_result,
            status_code=200,
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
            status_code=200,
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
            status_code=200,
        )
        result = FinnhubAPI(token)
        result = result.get_quote(symbol)

        assert result == expected_result
