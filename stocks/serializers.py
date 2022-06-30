from rest_framework import serializers

from stocks.models import StockSymbol


class StockSymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockSymbol
        fields = ["symbol"]


class CreateStockSymbolSerializer(serializers.Serializer):
    stock_symbols = serializers.ListField()

    def validate_stock_symbols(self, value):
        stock_symbols = StockSymbol.objects.filter(symbol__in=value).all()

        if len(value) != len(stock_symbols):
            db_stock_symbols = [symbol.symbol for symbol in stock_symbols]
            wrong_symbols = [
                symbol for symbol in value if symbol not in db_stock_symbols
            ]
            raise serializers.ValidationError(
                f"You have passed wrong symbols! {wrong_symbols}"
            )

        return stock_symbols
