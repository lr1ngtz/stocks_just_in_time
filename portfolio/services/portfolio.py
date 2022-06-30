def create_stock_symbols(portfolio, serializer) -> None:
    portfolio.stock_symbols.clear()
    portfolio.stock_symbols.add(*serializer.validated_data["stock_symbols"])
