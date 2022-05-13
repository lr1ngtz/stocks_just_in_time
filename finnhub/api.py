import requests

from core.constants import API_KEY, WRONG_SYMBOL_OUTPUT


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

        if not symbol:
            return {"response": "The symbol is required!"}

        response = requests.get(api_url)
        quote = response.json()

        if quote == WRONG_SYMBOL_OUTPUT:
            return {"response": "The symbol doesn't exist!"}

        return quote
