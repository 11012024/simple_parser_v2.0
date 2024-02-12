from concurrent.futures import ThreadPoolExecutor
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from driver_initializer import DriverInitializer
from selenium.webdriver.support import expected_conditions as EC

# Created: Friday, July 29, 2022, 12:22:10 PM


class PairsForCompareGetter:

    def __init__(self, xpaths, pairs_with_prices):
        self.__xpaths = xpaths
        self.__driver = DriverInitializer(self.__xpaths['url'], False).initialize_driver()
        self.__prices = pairs_with_prices

    def get_pairs_for_compare(self) -> dict:
        coins = self.__get_coins_without_dublicate(self.__xpaths['element_number'])
        if len(coins) > 100:
            sectors = [coins[x:x + 100] for x in range(0, len(coins), 100)]
            with ThreadPoolExecutor(max_workers=20) as executor:
                futures = []
                for sector in sectors:
                    futures.append(executor.submit(
                        SwapperParser(self.__xpaths).get_trading_pairs, sector))
                results = []
                for future in futures:
                    results.append(future.result())
                trading_pairs = {}
                for dictionary in results:
                    for pair_name, price in dictionary.items():
                        trading_pairs[pair_name] = price
        else:
            trading_pairs = SwapperParser(self.__xpaths).get_trading_pairs(coins)
        converted_pairs = self.__convert_pairs_to_usdt(trading_pairs)
        return converted_pairs

    def __get_coins_without_dublicate(self, element_number: int) -> list:
        try:
            self.__driver.find_element(By.XPATH, self.__xpaths['output_button']).click()
        except ElementClickInterceptedException:
            print('table is already opened!')
        finally:
            needed_step = 150
            all_coins_height = self.__driver.find_element(By.XPATH, self.__xpaths['visible_coins'] + '/div').size['height']
            coins_with_dublicate = self.__get_coins_with_dublicate(element_number, all_coins_height, needed_step)
            coins_without_dublicate = list(dict.fromkeys(coins_with_dublicate))
            self.__driver.quit()
            return coins_without_dublicate

    def __get_coins_with_dublicate(self, element_number: int, table_height: float, needed_step: float) -> list:
        table_with_coins = self.__driver.find_element(By.XPATH, self.__xpaths['visible_coins'])
        # Setting the start value for the start of scrolling
        current_height = 0
        coins_with_dublicate = []
        while current_height <= table_height:
            # since the content is dynamic we are getting
            # only that coins, which are available to us
            visible_coins = self.__driver.find_element(By.XPATH, self.__xpaths['visible_coins']).text.split('\n')[::element_number]
            for coin in visible_coins:
                coins_with_dublicate.append(coin)
            # scrolling down.
            self.__driver.execute_script("arguments[0].scrollTop = arguments[1]", table_with_coins, current_height)
            current_height += needed_step
        return coins_with_dublicate

    def __convert_pairs_to_usdt(self, trading_pairs: dict) -> dict:
        if self.__xpaths['quote'] == 'USDT':
            return trading_pairs
        quote_price_to_usdt = self.__prices[f"{self.__xpaths['quote']}/USDT"]
        converted_pairs = {}
        for pair_name, price in trading_pairs.items():
            converted_price = quote_price_to_usdt * price
            converted_pairs[pair_name] = converted_price
        return converted_pairs


class SwapperParser:

    def __init__(self, xpaths):
        self.__xpaths = xpaths
        self.__driver = DriverInitializer(self.__xpaths['url'], False).initialize_driver()

    def get_trading_pairs(self, coins):
        trading_pairs = {}
        switch_button = self.__driver.find_element(By.XPATH, self.__xpaths['switch_button'])
        self.__driver.find_element(By.XPATH, self.__xpaths['token_output']).send_keys('1')
        for coin in coins:
            try:
                self.__select_needed_coin(coin, self.__xpaths['output_button'])
                if self.__get_price_impact() <= 4:
                    trading_pairs[f'{coin}_buy'] = self.__get_price(self.__xpaths['token_input'])
                switch_button.click()
                if self.__get_price_impact() <= 4:
                    trading_pairs[f'{coin}_sell'] = self.__get_price(self.__xpaths['token_output'])
                switch_button.click()
            except TimeoutException:
                continue
            except ElementClickInterceptedException:
                continue
        self.__driver.quit()
        return trading_pairs

    def __select_needed_coin(self, coin: str, button_xpath: str):
        try:
            self.__driver.find_element(By.XPATH, button_xpath).click()
        except ElementClickInterceptedException:
            print('table is already opened!')
        finally:
            token_search_input = WebDriverWait(self.__driver, 3).until(EC.presence_of_element_located((By.XPATH, self.__xpaths['search_token'])))
            if len(token_search_input.get_attribute('value')) != 0:
                token_search_input.clear()
            token_search_input.send_keys(coin)
            WebDriverWait(self.__driver, 2).until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(),'{coin}')]"))).click()

    def __get_price(self, for_tokens_field: str) -> float:
        return float(WebDriverWait(self.__driver, 3).until(
            lambda wd: wd.find_element(By.XPATH, for_tokens_field).get_attribute('value')))

    def __get_price_impact(self) -> float:
        if 'price_impact_button' in self.__xpaths:
            WebDriverWait(self.__driver, 2).until(EC.element_to_be_clickable((By.XPATH, self.__xpaths['price_impact_button']))).click()
        if 'price_impact' in self.__xpaths:
            return float(WebDriverWait(self.__driver, 2).until(
                lambda wd: wd.find_element(By.XPATH, self.__xpaths['price_impact']).text.replace('%', '').replace('<', '')))
        else:
            return 0
