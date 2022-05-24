from datetime import datetime
from stocks.exceptions import UnexpectedQuoteInfoException

from stocks.models import StockSymbol


def map_finnhub_api_quote(quote_info: dict, stock_symbol: StockSymbol) -> dict:
    mandatory_keys = ("c", "d", "dp", "h", "l", "o", "pc", "t")

    for key in quote_info:
        if key not in mandatory_keys:
            raise UnexpectedQuoteInfoException()

    if quote_info.get("t"):
        quote_info["t"] = datetime.fromtimestamp(quote_info["t"])

    mapped_quote_info = {
        "current_price": quote_info.get("c"),
        "change": quote_info.get("d"),
        "percent_change": quote_info.get("dp"),
        "high_price_of_the_day": quote_info.get("h"),
        "low_price_of_the_day": quote_info.get("l"),
        "open_price_of_the_day": quote_info.get("o"),
        "previous_close_price": quote_info.get("pc"),
        "timestamp": quote_info.get("t"),
        "stock_symbol": stock_symbol,
    }

    return mapped_quote_info
