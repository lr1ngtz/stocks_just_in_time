import requests

from finnhub.exceptions import FinnhubAPIException


class FinnhubAPI:
    """
    Class is responsible for obtaining stocks, symbols and etc.
    from Finnhub API.
    """

    token = None
    base_url = "https://finnhub.io/api/v1/"

    def __init__(self, token) -> None:
        self.token = token

    def get_stocks(self) -> list:
        """
        Call the API in order to obtain info about all available stocks.

        output example: [
        {
            "currency": "USD",
            "description": "JERRICK MEDIA HOLDINGS -CW25",
            "displaySymbol": "CRTDW",
            "figi": "BBG00X7KXFL2",
            "isin": null,
            "mic": "XNAS",
            "shareClassFIGI": "",
            "symbol": "CRTDW",
            "symbol2": "",
            "type": "Equity WRT"
        },
        {
            ...
        },
        ]
        keys info https://finnhub.io/docs/api/stock-symbols
        """
        api_url = f"{self.base_url}stock/symbol?exchange=US&token={self.token}"

        return self._send_get(api_url)

    def get_quote(self, symbol: str) -> dict:
        """
        Call the API in order to obtain specified symbol info.

        args: symbol -> str

        output example: {
            "c": 147.11,
            "d": 4.55,
            "dp": 3.1916,
            "h": 148.1,
            "l": 143.11,
            "o": 144.59,
            "pc": 142.56,
            "t": 1652472004
        }
        keys info https://finnhub.io/docs/api/quote
        """
        api_url = f"{self.base_url}quote?symbol={symbol}&token={self.token}"

        return self._send_get(api_url)

    def _send_get(self, url: str):
        """
        Sends request to the passed url and returns
        json response.
        """
        try:
            response = requests.get(url)
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.RequestException,
        ) as err:
            raise FinnhubAPIException(err)

        if response.status_code in (401, 429, 500):
            error = response.json()
            raise FinnhubAPIException(error["error"])

        api_data = response.json()

        return api_data
