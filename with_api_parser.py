from high_volumes_getter import ThroughVolumeSelector
from to_usdt_converter import Converter
from enum import Enum
import requests


# Created: Monday, July 11, 2022, 12:09:39 PM

class PageResponce(Enum):

    error = 204


class WebInfoGetter:

    def __init__(self, url: str):
        self.__url = url

    def get_response(self):
        response = requests.get(self.__url)
        # responce.rise_for_status()
        # returns an HTTPError object if an error
        # has occurred during the process. It is
        # used for debugging the requests module
        # and is an integral part of Python requests.
        response.raise_for_status()
        if response.status_code != PageResponce.error.value:
            return response.json()


class ApiPairsGetter:
    """ Exchange APIs are a way for traders to access their
      exchange account programmatically, so they can trade without logging
      into the exchange. With APIs, traders can use 3rd party services
      to execute trades, manage their portfolio, collect data on their account,
      and implement complex strategies. """

    # 11/07/2022, 11:22 pm...
    # Tomorrow I will go to my grandmother for her birthday
    # yesterday I saw her(about 7:50-8:10 pm) and listened Miyagi(Fade, Salun)...
    # And very soon I'll become tall!

    def get_pairs_for_compare(self, volumes, prices):
        converted_volumes = Converter(volumes, prices).convert_pairs_to_usdt(0)
        trading_pairs = {}
        for pair_name in ThroughVolumeSelector(converted_volumes).pairs_with_high_volumes:
            trading_pairs[pair_name] = prices[pair_name]
        return Converter(trading_pairs, prices).convert_pairs_to_usdt(1)


class AAX:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://api.aax.com/v2/market/tickers').get_response()
        symbols = WebInfoGetter(url='https://api.aax.com/v2/instruments').get_response()
        for ticker in tickers['tickers']:
            for symbol in symbols['data']:
                if ticker['s'] == symbol['symbol']:
                    clear_name = f"{symbol['base']}/{symbol['quote']}"
                    prices[clear_name] = ticker['c']
                    volumes[clear_name] = ticker['q']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class FMFW:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://api.fmfw.io/api/3/public/ticker').get_response()
        symbols = WebInfoGetter(url='https://api.fmfw.io/api/3/public/symbol').get_response()
        for symbol in symbols:
            for ticker in tickers:
                if symbol == ticker:
                    try:
                        clear_name = symbols[symbol]['base_currency'] + '/' + symbols[symbol]['quote_currency']
                        prices[clear_name] = tickers[ticker]['last']
                        volumes[clear_name] = tickers[ticker]['volume']
                    except TypeError:
                        continue
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class Tapbit:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://openapi.tapbit.com/spot/api/spot/market/summary').get_response()
        for ticker in tickers:
            print(ticker['base_currency'] + '/' + ticker['quote_currency'] + ' ' + ticker['last_price'])
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class Digifinex:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://openapi.digifinex.com/v3/ticker').get_response()
        for ticker in tickers['ticker']:
            clear_name = ticker['symbol'].replace('_', '/').upper()
            prices[clear_name] = ticker['last']
            volumes[clear_name] = ticker['vol']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class BingX:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://api-swap-rest.bingbon.pro/api/v1/market/getTicker').get_response()
        for ticker in tickers['data']['tickers']:
            clear_name = ticker['symbol'].replace('-', '/')
            prices[clear_name] = ticker['lastPrice']
            volumes[clear_name] = ticker['volume']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class BKEX:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://api.bkex.com/v2/q/tickers').get_response()
        for ticker in tickers['data']:
            clear_name = ticker['symbol'].replace('_', '/')
            prices[clear_name] = ticker['close']
            volumes[clear_name] = ticker['volume']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class BigONE:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://big.one/api/v3/asset_pairs/tickers').get_response()
        for ticker in tickers['data']:
            clear_name = ticker['asset_pair_name'].replace('-', '/')
            prices[clear_name] = ticker['close']
            volumes[clear_name] = ticker['volume']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class AscendEX:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://ascendex.com/api/pro/v1/spot/ticker').get_response()
        for ticker in tickers['data']:
            clear_name = ticker['symbol']
            prices[clear_name] = ticker['close']
            volumes[clear_name] = ticker['volume']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class LBank:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://api.lbkex.com/v1/ticker.do?symbol=all').get_response()
        for ticker in tickers:
            clear_name = ticker['symbol'].replace('_', r'/').upper()
            prices[clear_name] = ticker['ticker']['latest']
            volumes[clear_name] = ticker['ticker']['vol']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class Bitrue:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://openapi.bitrue.com/api/v1/ticker/24hr').get_response()
        symbols = WebInfoGetter(url='https://openapi.bitrue.com/api/v1/exchangeInfo').get_response()
        for symbol in symbols['symbols']:
            for ticker in tickers:
                if ticker['symbol'] == symbol['symbol']:
                    clear_name = symbol['baseAsset'].upper() + '/' + symbol['quoteAsset'].upper()
                    prices[clear_name] = ticker['lastPrice']
                    volumes[clear_name] = ticker['volume']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class Huobi:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://api.huobi.com/market/tickers').get_response()
        symbols = WebInfoGetter(url='https://api.huobi.com/v2/settings/common/symbols').get_response()
        for symbol in symbols['data']:
            for ticker in tickers['data']:
                if ticker['symbol'] == symbol['sc']:
                    clear_name = symbol['bcdn'] + '/' + symbol['qcdn']
                    prices[clear_name] = ticker['bid']
                    volumes[clear_name] = ticker['amount']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class Bybit:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://api.bybit.com/spot/quote/v1/ticker/24hr').get_response()
        symbols = WebInfoGetter(url='https://api.bybit.com/spot/v1/symbols').get_response()
        for symbol in symbols['result']:
            for ticker in tickers['result']:
                if ticker['symbol'] == symbol['name']:
                    clear_name = symbol['baseCurrency'] + '/' + symbol['quoteCurrency']
                    prices[clear_name] = ticker['lastPrice']
                    volumes[clear_name] = ticker['volume']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class HotCoin:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://api.hotcoinfin.com/v1/market/ticker').get_response()
        for ticker in tickers['ticker']:
            clear_name = ticker['symbol'].upper().replace('_', r'/')
            prices[clear_name] = ticker['last']
            volumes[clear_name] = ticker['vol']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class Kucoin:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://api.kucoin.com/api/v1/market/allTickers').get_response()
        for ticker in tickers['data']['ticker']:
            clear_name = ticker['symbol'].replace('-', r'/')
            if clear_name.split('/')[1] != 'PAX':
                prices[clear_name] = ticker['last']
                volumes[clear_name] = ticker['vol']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class WhiteBit:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://whitebit.com/api/v4/public/ticker').get_response()
        for ticker in tickers:
            clear_name = ticker.replace('_', r'/')
            prices[clear_name] = tickers[ticker]['last_price']
            volumes[clear_name] = tickers[ticker]['base_volume']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class MEXC:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://www.mexc.com/open/api/v2/market/ticker').get_response()
        for ticker in tickers['data']:
            clear_name = ticker['symbol'].replace('_', r'/')
            prices[clear_name] = ticker['last']
            volumes[clear_name] = ticker['volume']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class OKX:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://www.okx.com/api/v5/market/tickers?instType=SPOT').get_response()
        for ticker in tickers['data']:
            clear_name = ticker['instId'].replace('-', r'/')
            prices[clear_name] = ticker['last']
            volumes[clear_name] = ticker['vol24h']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class XT:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://www.xt.pub/exchange/api/markets/returnTicker').get_response()
        for ticker in tickers:
            clear_name = ticker.replace('_', r'/')
            try:
                prices[clear_name] = tickers[ticker]['last']
                volumes[clear_name] = tickers[ticker]['baseVolume']
            except KeyError:
                continue
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class Exmo:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://api.exmo.com/v1.1/ticker').get_response()
        for ticker in tickers:
            clear_name = ticker.replace('_', r'/')
            if clear_name.split('/')[1] != 'KZT':
                prices[clear_name] = tickers[ticker]['last_trade']
                volumes[clear_name] = tickers[ticker]['vol']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)


class Poloniex:

    def get_trading_pairs(self):
        prices, volumes = {}, {}
        tickers = WebInfoGetter(url='https://api.poloniex.com/markets/ticker24h').get_response()
        for ticker in tickers:
            clear_name = ticker['displayName']
            prices[clear_name] = ticker['close']
            volumes[clear_name] = ticker['quantity']
        return ApiPairsGetter().get_pairs_for_compare(volumes, prices)
