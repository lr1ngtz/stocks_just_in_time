import requests


class FinnhubAPI:
    token = None
    base_url = "https://finnhub.io/api/v1/"

    def __init__(self, token) -> None:
        self.token = token

    def get_stocks(self) -> list:
        api_url = f"{self.base_url}stock/symbol?exchange=US&token={self.token}"

        return self._send_get(api_url)

    def get_quote(self, symbol: str) -> dict:
        api_url = f"{self.base_url}quote?symbol={symbol}&token={self.token}"

        return self._send_get(api_url)

    def _send_get(self, url):
        response = requests.get(url)
        api_data = response.json()

        return api_data
