# Created: Sunday, June 19, 2022, 12:37:17 PM


class Comparer:

    def __init__(self, current_coin_pairs: dict):
        # all trading pairs of current coin from all exchanges.
        self.__current_coin_pairs = current_coin_pairs

    def find_arbitrage_opportunities(self):
        arbitrage = {}
        for exchange, exchange_pairs in self.__current_coin_pairs.items():
            for pair_name, price in exchange_pairs.items():
                # after getting current pair price, we are
                # starting sorting out other pairs with current coin
                # for finding difference betweeen first and second prices
                for exchange_2, exchange_2_pairs in self.__current_coin_pairs.items():
                    for pair_name_2, price_2 in exchange_2_pairs.items():
                        if price != price_2:
                            price_for_sell = max(price, price_2)
                            price_for_buy = min(price, price_2)
                            difference = self.__get_difference(for_sell=price_for_sell, for_buy=price_for_buy)
                            if 3 <= difference <= 100:
                                if price_for_buy == price:
                                    arbitrage[f'{difference}%'] = f'{exchange} {pair_name} {exchange_2} {pair_name_2}'
                                elif price_for_buy == price_2:
                                    arbitrage[f'{difference}%'] = f'{exchange_2} {pair_name_2} {exchange} {pair_name}'
        if len(arbitrage) != 0:
            for difference, opportunity in arbitrage.items():
                print(difference, opportunity)

    def __get_difference(self, for_sell: float, for_buy: float) -> float:
        difference = round(for_sell / for_buy * 100 - 100, 2)
        return difference
