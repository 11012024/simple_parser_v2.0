import requests

# Created: Friday, June 24, 2022, 8:13:31 PM


class SymbolsGetter:

    # Parameters that are appended to the URL
    # from 1 to n coins from CoinMarketCap
    __params = {
        'start': '1',
        'limit': '5000'
    }
    """
    An Application Program Interface (API) Key is like a complex
    username and password system made up of an API Key,
    API Passphrase, and API Secret that allows the program
    of your choice to “communicate” with your trading exchange or wallet.
    """
    __api_key = '4e28b49d-205f-4022-8471-965ff12178d2'

    """
    API headers are like an extra source of information for each API call you make.
    Their job is to represent the meta-data associated with an API request and response. 
    If you ever encounter issues with an API, 
    the first place you should look is the headers, 
    since they can help you track down any potential issues.
    """
    _headers = {
        'X-CMC_PRO_API_KEY': __api_key,
        'Accepts': 'application/json'
    }

    def get_api_data(self) -> list:
        # getting all data about top n coins.
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        json = requests.get(url, params=self.__params, headers=self._headers).json()
        all_data = json['data']
        symbols = []
        # adding all needed symbols to the list.
        for coin in all_data:
            symbols.append(coin['symbol'])
        # returning top n coins symbols
        return symbols
