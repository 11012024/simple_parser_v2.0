from high_volumes_getter import ThroughVolumeSelector
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_initializer import DriverInitializer

# Created: Monday, July 4, 2022, 5:11:57 PM


class WebInfoParser:

    def __init__(self, exchange: str):
        base_url = 'https://coinmarketcap.com/exchanges/'
        self.__driver = DriverInitializer(base_url + exchange, headless=True).initialize_driver()

    def get_web_info(self, click_count: float) -> list:
        # checking, if on current exchange more than 100
        # pairs are traded if it is so, we call method that
        # will scroll to the page bottom and click on the button
        if click_count > 0:
            self.__load_all_pairs(click_count=click_count)
        xpath = '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[1]/div/table/tbody'
        # finding table with all crypto
        trading_pairs_info = self.__driver.find_element(By.XPATH, xpath).text.split('\n')[2::]
        self.__driver.quit()
        return trading_pairs_info

    def __load_all_pairs(self, click_count: float):
        # for load all exchange pairs, we need
        # to click on the "load more" button
        # and then will be loaded one more 100 pairs(or less))
        counter = 1
        while counter <= click_count:
            self.__click_on_the_button()
            WebDriverWait(self.__driver, 7).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/button')))
            counter += 1

    def __click_on_the_button(self):
        # Scroll down to the bottom of the webpage
        self.__driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.__driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div[2]/button').click()


class CoinMPairsGetter:

    def get_trading_pairs(self, exchange, click_count) -> dict:
        trading_pairs_info = WebInfoParser(exchange).get_web_info(click_count)
        # in this dictionary will be that pairs with
        # prices, which volumes bigger than given number
        trading_pairs = {}
        for pair_with_volume in PairsWithVolumesGetter(trading_pairs_info).get_pairs_with_volumes():
            for pair_name, price in PairsWithPricesGetter(trading_pairs_info).get_pairs_with_prices().items():
                if pair_name == pair_with_volume:
                    trading_pairs[pair_name] = price
        # for future compare we need that all prices would be the float type
        # because we will calculate difference between prices...
        trading_pairs = ToFloatConverter(trading_pairs).convert_to_float()
        return trading_pairs


class PairsNamesGetter:

    def __init__(self, trading_pairs_info: list):
        self._trading_pairs_info = trading_pairs_info

    def get_clean_pairs_names(self) -> list:
        clean_pairs_names = self._trading_pairs_info[::9]
        return clean_pairs_names


class PairsWithPricesGetter:

    def __init__(self, trading_pairs_info: list):
        self._trading_pairs_info = trading_pairs_info

    def get_pairs_with_prices(self) -> dict:
        clean_pairs_names = PairsNamesGetter(self._trading_pairs_info).get_clean_pairs_names()
        clean_prices = self.__get_clean_prices()
        pairs_with_prices = dict(zip(clean_pairs_names, clean_prices))
        pairs_with_prices = FromStrangeValuesCleaner(pairs_with_prices).remove_strange_values()
        return pairs_with_prices

    def __get_clean_prices(self) -> list:
        unclean_prices = self._trading_pairs_info[1::][::9]
        clean_prices = []
        for price in unclean_prices:
            clean_prices.append(price.replace('$', '').replace(',', ''))
        return clean_prices


class PairsWithVolumesGetter:

    def __init__(self, trading_pairs_info: list):
        self.__trading_pairs_info = trading_pairs_info

    # getting 24 hour trading volume of every pair
    def get_pairs_with_volumes(self) -> dict:
        clean_pairs = PairsNamesGetter(self.__trading_pairs_info).get_clean_pairs_names()
        clean_volumes = self.__get_clean_volumes()
        pairs_with_volumes = dict(zip(clean_pairs, clean_volumes))
        pairs_with_volumes = FromStrangeValuesCleaner(pairs_with_volumes).remove_strange_values()
        pairs_with_volumes = ThroughVolumeSelector(pairs_with_volumes).pairs_with_high_volumes
        return pairs_with_volumes

    def __get_clean_volumes(self) -> list:
        unclean_volumes = self.__trading_pairs_info[3::][::9]
        clean_volumes = []
        for price in unclean_volumes:
            clean_volumes.append(price.replace('$', '').replace(',', ''))
        return clean_volumes


class FromStrangeValuesCleaner:

    def __init__(self, pairs_with_values: dict):
        self.__pairs_with_values = pairs_with_values

    def remove_strange_values(self) -> dict:
        need_remove = []
        for pair_name, value in self.__pairs_with_values.items():
            if any(symbol in value for symbol in ['-', '*', '<']) or value == '0':
                need_remove.append(pair_name)
        for pair in need_remove:
            self.__pairs_with_values.pop(pair)
        return self.__pairs_with_values


class ToFloatConverter:

    def __init__(self, pairs_with_prices: dict):
        self.__pairs_with_prices = pairs_with_prices

    def convert_to_float(self) -> dict:
        for pair_name, price in self.__pairs_with_prices.items():
            self.__pairs_with_prices[pair_name] = float(price)
        return self.__pairs_with_prices
