# Created: Saturday, July 9, 2022, 4:57:31 PM

class Converter:

    """ In this class I'll convert the prices
    of pairs whose quote currency is not USDT.
    This is necessary for the future finding of the
    difference between prices for the same coin on different exchanges. """

    def __init__(self, pairs_for_convert: dict, pairs_with_prices: dict):
        self.__pairs_for_convert = pairs_for_convert
        self.__pairs_with_prices = pairs_with_prices
        self.__pairs_for_return = {}

    def convert_pairs_to_usdt(self, currency_number: float) -> dict:
        for pair_name, value in self.__pairs_for_convert.items():
            quote_and_base = pair_name.split('/')
            # If number is 0, than we are calculating values
            # using base currency, if 1 - using quote =)
            if currency_number == 1:
                # check, if pair quote or base currency is not
                # a stablecoin because we don't need to convert
                # the volume or price to usdt which is already converted to usdt
                if quote_and_base[1] != 'USDT':
                    self.__finding_price_to_usdt(quote_and_base[currency_number], pair_name)
                else:
                    self.__pairs_for_return[pair_name] = float(value)
            elif currency_number == 0:
                self.__finding_price_to_usdt(quote_and_base[currency_number], pair_name)
        return self.__pairs_for_return

    def __finding_price_to_usdt(self, quote: str, pair: str):
        # trying to find price of quote currency to usdt in current exchange
        if f"USDT/{quote}" in self.__pairs_with_prices:
            self.__convert_value_to_usdt(quote_pair=f"USDT/{quote}", action=self.__get_math_action('/'), pair=pair)
        elif f"{quote}/USDT" in self.__pairs_with_prices:
            self.__convert_value_to_usdt(quote_pair=f"{quote}/USDT", action=self.__get_math_action('*'), pair=pair)

    # returning math action for passing her as parameter to the
    # method, where we will calculate pair volume/price to usdt using
    # quote price to usdt and pair volume/price to quote currency
    def __get_math_action(self, action: str):
        if action == '/':
            return lambda x, y: x / y
        elif action == '*':
            return lambda x, y: x * y

    # Taking pair volume/price to usdt using quote currency.
    # We are finding price of quote currency to usdt
    # in current exchange and calculating pair volume/price to usdt =)
    def __convert_value_to_usdt(self, quote_pair: str, action, pair: str):
        # volume of pair with quote currency which is not an usdt
        value_for_convert = float(self.__pairs_for_convert[pair])
        # getting price to usdt of quote currency
        quote_price_to_usdt = float(self.__pairs_with_prices[quote_pair])
        # calculating pair volume/price to usdt
        converted_value = action(value_for_convert, quote_price_to_usdt)
        # updating pair volume/price
        self.__pairs_for_return[pair] = converted_value
