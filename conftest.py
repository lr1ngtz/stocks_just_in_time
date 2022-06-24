import pytest
from rest_framework.test import APIClient

from factories import PortfolioFactory, StockSymbolFactory, UserFactory


@pytest.fixture
def apple_stock():
    stock_symbol = StockSymbolFactory(symbol="AAPL")
    return stock_symbol


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def user():
    user = UserFactory()
    return user


@pytest.fixture
def portfolio():
    portfolio = PortfolioFactory()
    return portfolio
