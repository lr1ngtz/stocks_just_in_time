import factory

from stocks.models import StockSymbol


class StockSymbolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StockSymbol
