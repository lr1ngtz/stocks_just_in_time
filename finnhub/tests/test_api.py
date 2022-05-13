from unittest.mock import patch

import requests

from finnhub.api import FinnhubConnection


class MockResponse:
    @staticmethod
    def json():
        return {"m_key": "m_value"}


def test_FinnhubConnection_get_stocks__api_key_absence():
    with patch.object(FinnhubConnection, "api_key", return_value=None):
        result = FinnhubConnection()
        result = result.get_stocks()
        expected_result = {"error": "Invalid API key"}
        assert result == expected_result


def test_FinnhubConnection_get_stocks__success(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = FinnhubConnection()
    result = result.get_stocks()
    assert result["m_key"] == "m_value"


def test_FinnhubConnection_get_quote__api_key_absence():
    with patch.object(FinnhubConnection, "api_key", return_value=None):
        result = FinnhubConnection()
        result = result.get_quote("AAPL")
        expected_result = {"error": "Invalid API key"}
        assert result == expected_result


def test_FinnhubConnection_get_quote__empty_symbol():
    result = FinnhubConnection()
    result = result.get_quote("")
    expected_result = {"response": "The symbol is required!"}
    assert result == expected_result


def test_FinnhubConnection_get_quote__wrong_symbol():
    result = FinnhubConnection()
    result = result.get_quote("some_symbol")
    expected_result = {"response": "The symbol doesn't exist!"}
    assert result == expected_result


def test_FinnhubConnection_get_quote__success(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = FinnhubConnection()
    result = result.get_quote("AAPL")
    assert result["m_key"] == "m_value"
