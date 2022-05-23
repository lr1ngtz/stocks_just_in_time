from datetime import datetime


def map_finnhub_api_quote(quote_info: dict) -> dict:
    if quote_info.get("t"):
        quote_info["t"] = datetime.fromtimestamp(quote_info["t"])

    return quote_info
