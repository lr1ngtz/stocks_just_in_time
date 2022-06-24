import pytest

from stocks.serializers import StockSymbolSerializer, CreateStockSymbolSerializer


@pytest.mark.django_db
def test_StockSymbolSerializer__success(apple_stock):
    data = {"symbol": apple_stock.symbol}
    serializer = StockSymbolSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    assert serializer.validated_data == data


@pytest.mark.django_db
def test_StockSymbolSerializer__wrong_input():
    data = {"some": ["wrong", "data"]}
    serializer = StockSymbolSerializer(data=data)
    serializer.is_valid()
    assert "symbol" in serializer.errors.keys()


@pytest.mark.django_db
def test_StockSymbolSerializer__wrong_data():
    data = {"symbol": ["wrong", "data"]}
    serializer = StockSymbolSerializer(data=data)
    serializer.is_valid()
    assert "symbol" in serializer.errors.keys()


@pytest.mark.django_db
def test_CreateStockSymbolSerializer__success(apple_stock):
    data = {"stock_symbols": ["AAPL"]}
    serializer = CreateStockSymbolSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    expected_result = {"stock_symbols": [apple_stock]}
    assert serializer.data == expected_result


@pytest.mark.django_db
def test_CreateStockSymbolSerializer__wrong_data():
    data = {"stock_symbols": ["WRONG", "SYMBOLS"]}
    serializer = CreateStockSymbolSerializer(data=data)
    serializer.is_valid()
    assert "stock_symbols" in serializer.errors.keys()
