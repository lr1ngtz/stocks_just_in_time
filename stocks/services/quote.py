from django.conf import settings

from stocks.models import Quote, StockSymbol
from finnhub.api import FinnhubAPI
from stocks.services.map_finnhub_api_quote import map_finnhub_api_quote


def create_quote(symbol: str):
    finnhub_api = FinnhubAPI(settings.FINNHUB_API_KEY)
    finnhub_quote = finnhub_api.get_quote(symbol)
    stock_symbol = StockSymbol.objects.filter(symbol=symbol).first()
    if stock_symbol:
        finnhub_quote = map_finnhub_api_quote(finnhub_quote, stock_symbol)
        Quote.objects.create(**finnhub_quote)
