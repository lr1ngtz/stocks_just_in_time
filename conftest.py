import pytest

from factories import StockSymbolFactory


@pytest.fixture
def apple_stock():
    stock_symbol = StockSymbolFactory(symbol="AAPL")
    return stock_symbol
