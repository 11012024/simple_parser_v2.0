from comparer import Comparer
from all_pairs_getter import AllPairsGetter
from coinM_data_getter import SymbolsGetter

# Created: Saturday, July 9, 2022, 4:58:41 PM


class ForCompareSelector:

    def __init__(self):
        self.__top_n_coins = SymbolsGetter().get_api_data()

    def selection_for_compare(self, all_pairs):
        for coin in self.__top_n_coins:
            current_coin_pairs = {}
            for exchange_name, exchange_pairs in all_pairs.items():
                # creating dictionary for all pairs
                # with current coin on current exchange
                current_exchange_pairs = {}
                for pair_name, price in exchange_pairs.items():
                    base_currency = pair_name.split('/')[0]
                    # if base currency is current coin, bring
                    # current pair to the current_exchange_pairs dictionary
                    if base_currency == coin:
                        current_exchange_pairs[pair_name] = price
                # bring current exchange with all pairs of current
                # coin to the current_coin_pairs dictionary for future compare
                current_coin_pairs[exchange_name] = current_exchange_pairs
            Comparer(current_coin_pairs).find_arbitrage_opportunities()


ForCompareSelector().selection_for_compare(AllPairsGetter().get_all_pairs())
