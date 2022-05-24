import pytest

from factories import StockSymbolFactory


@pytest.fixture
def stock_symbol():
    stock_symbol = StockSymbolFactory(symbol="AAPL")
    return stock_symbol
