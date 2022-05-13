import requests

from core.constants import API_KEY


class FinnhubConnection:
    api_key = API_KEY

    def get_stocks(self) -> list:
        api_url = (
            f"https://finnhub.io/api/v1/stock/symbol?exchange=US&token={self.api_key}"
        )
        response = requests.get(api_url)
        stocks = response.json()
        return stocks

    def get_quote(self, symbol: str) -> dict:
        api_url = (
            f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={self.api_key}"
        )
        response = requests.get(api_url)
        quote = response.json()
        return quote
