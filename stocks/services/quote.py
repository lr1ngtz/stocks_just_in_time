from django.conf import settings

from stocks.models import Quote, StockSymbol
from finnhub.api import FinnhubAPI
from stocks.services.map_finnhub_api_quote import map_finnhub_api_quote


def create_quote(symbol: str) -> Quote:
    finnhub_api = FinnhubAPI(settings.FINNHUB_API_KEY)
    finnhub_quote = finnhub_api.get_quote(symbol)
    finnhub_quote = map_finnhub_api_quote(finnhub_quote)
    stock_symbol = StockSymbol.objects.get(symbol=symbol)
    quote = Quote.objects.save_quote(
        current_price=finnhub_quote.get("c"),
        change=finnhub_quote.get("d"),
        percent_change=finnhub_quote.get("dp"),
        high_price_of_the_day=finnhub_quote.get("h"),
        low_price_of_the_day=finnhub_quote.get("l"),
        open_price_of_the_day=finnhub_quote.get("o"),
        previous_close_price=finnhub_quote.get("pc"),
        timestamp=finnhub_quote.get("t"),
        stock_symbol=stock_symbol,
    )

    return quote
