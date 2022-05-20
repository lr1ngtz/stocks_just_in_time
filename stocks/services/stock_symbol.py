from django.conf import settings

from stocks.models import StockSymbol
from finnhub.api import FinnhubAPI


def create_or_update_stock_symbol() -> dict:
    finnhub_api = FinnhubAPI(settings.FINNHUB_API_KEY)
    finnhub_stock_symbols = finnhub_api.get_stocks()
    info = {"created": 0, "updated": 0}
    for symbol in finnhub_stock_symbols:
        obj, created = StockSymbol.objects.update_or_create(
            symbol=symbol.get("symbol"),
            defaults={
                "description": symbol.get("description"),
                "display_symbol": symbol.get("displaySymbol"),
                "figi": symbol.get("figi"),
                "isin": symbol.get("isin"),
                "mic": symbol.get("mic"),
                "share_class_figi": symbol.get("shareClassFIGI"),
                "symbol2": symbol.get("symbol2"),
                "type": symbol.get("type"),
            },
        )

        if created:
            info["created"] += 1
        else:
            info["updated"] += 1

    return info
