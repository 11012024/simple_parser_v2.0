import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from high_volumes_getter import ThroughVolumeSelector
import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# Created: Sunday, September 4, 2022, 5:37:16 PM

class DriverInitializer:

    """ Selenium WebDriver is an automated testing
    framework used for the validation of websites
    (and web applications). It supports popular programming
    languages such as Python, C#, Java, Ruby, and more. """

    def __init__(self, url: str, headless: bool):
        self.__url = url
        self.__headless = headless

    def initialize_driver(self):
        executable_path = pathlib.Path('chromedriver.exe').absolute().__str__()
        webdriver_options = self.__get_driver_options()
        chrome_driver = webdriver.Chrome(service=Service(executable_path=executable_path), options=webdriver_options)
        chrome_driver.get(self.__url)
        # giving to webpage n seconds for her boot
        chrome_driver.implicitly_wait(7)
        return chrome_driver

    def __get_driver_options(self):
        options = Options()
        options.headless = self.__headless
        return options


class Phemex:

    def _get_web_info(self, page_url, table_xpath):
        driver = DriverInitializer(page_url, True).initialize_driver()
        driver.maximize_window()
        time.sleep(5)
        crypto_table = driver.find_element(By.XPATH, table_xpath).text
        driver.quit()
        return crypto_table

    def get_trading_pairs(self):
        table_xpath = '/html/body/div[2]/div[4]/div'
        crypto_table = self._get_web_info('https://phemex.com/ru/markets?tabType=Spot', table_xpath)
        pairs_names = self.__get_pairs_names(crypto_table)
        turnovers = self.__get_turnovers(crypto_table)
        pairs_with_volumes = dict(zip(pairs_names, turnovers))
        pairs_with_high_volumes = ThroughVolumeSelector(self.__remove_pairs(pairs_with_volumes)).pairs_with_high_volumes
        prices = self.__get_prices(crypto_table)
        pairs_with_prices = dict(zip(pairs_names, prices))
        trading_pairs = {}
        for pair_name in ThroughVolumeSelector(pairs_with_high_volumes).pairs_with_high_volumes:
            trading_pairs[pair_name] = pairs_with_prices[pair_name]
        return ToFloatConverter(trading_pairs).convert_to_float()

    def __get_pairs_names(self, crypto_table):
        unclear_names = crypto_table.split('\n')[18::][0::2][::4]
        clear_pairs = []
        for name in unclear_names:
            base_and_quote = name.split(' / ')
            clear_pairs.append(f'{base_and_quote[0]}/{base_and_quote[1]}')
        return clear_pairs

    def __get_turnovers(self, crypto_table):
        unclean_turnovers = crypto_table.split('\n')[21::][::8]
        clean_turnovers = []
        for turnover in unclean_turnovers:
            clean_turnovers.append(turnover.replace('$ ', r'').replace(',', r''))
        return clean_turnovers

    def __get_prices(self, crypto_table):
        prices = crypto_table.split('\n')[18:][0::2][1:][::4]
        return prices

    def __remove_pairs(self, pairs: dict):
        need_remove = []
        for pair_name, value in pairs.items():
            if value == '--':
                need_remove.append(pair_name)
        for pair in need_remove:
            pairs.pop(pair)
        return pairs


class ToFloatConverter:

    def __init__(self, pairs_with_prices: dict):
        self.__pairs_with_prices = pairs_with_prices

    def convert_to_float(self) -> dict:
        for pair_name, price in self.__pairs_with_prices.items():
            self.__pairs_with_prices[pair_name] = float(price)
        return self.__pairs_with_prices


class CoinW:

    def _get_web_info(self, page_url, table_xpath):
        driver = DriverInitializer(page_url, True).initialize_driver()
        driver.maximize_window()
        crypto_table = WebDriverWait(driver, 2).until(lambda wd: wd.find_element(By.XPATH, table_xpath).text)
        driver.quit()
        return crypto_table

    def get_trading_pairs(self):
        table_xpath = '//*[@id="coinw"]/div/div/div[2]/div[4]/div[1]/div[3]/table/tbody'
        crypto_table = self._get_web_info('https://www.coinw.com/front/market', table_xpath)
        crypto_table = [elem for elem in crypto_table.split('\n') if elem != 'R&S']
        pairs_names = crypto_table[::9]
        prices = crypto_table[1::][::9]
        trading_pairs = dict(zip(pairs_names, prices))
        return ToFloatConverter(trading_pairs).convert_to_float()


class DeepCoin:

    def get_trading_pairs(self):
        driver = DriverInitializer('https://www.deepcoin.com/en/markets', True).initialize_driver()
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[1]/ul/li[2]').click()
        table_xpath = '//*[@id="app"]/div[2]/div[2]/div/div[3]/div[2]'
        button = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[4]/button[2]')
        page_count = 1
        dictionaries = []
        while page_count <= 9:
            time.sleep(2)
            crypto_table = WebDriverWait(driver, 5).until(lambda wd: wd.find_element(By.XPATH, table_xpath).text).split('\n')
            names = crypto_table[::5]
            prices = crypto_table[2::][::5]
            dictionaries.append(dict(zip(names, prices)))
            button.click()
            page_count += 1
        pairs = {}
        for sector in dictionaries:
            for name, price in sector.items():
                pairs[name.replace('USDT', r'/USDT')] = float(price)
        driver.quit()
        return pairs


class Biswap:

    def get_trading_pairs(self):
        driver = DriverInitializer('https://biswap.org/analytics/tokens', False).initialize_driver()
        driver.maximize_window()
        table_xpath = '//*[@id="root"]/div[1]/div[2]/div/div/div[2]/div[4]'
        button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div[2]/div[4]/div[2]/div/ul/li[8]/a')
        page_count = 1
        while page_count <= 5:
            crypto_table = WebDriverWait(driver, 5).until(lambda wd: wd.find_element(By.XPATH, table_xpath).text.split('\n'))
            crypto_table = crypto_table[:len(crypto_table) - 5]
            print(crypto_table[7::])
            button.click()
            page_count += 1
        driver.quit()


class SpookySwap:

    def get_trading_pairs(self):
        driver = DriverInitializer('https://info.spooky.fi/tokens', False).initialize_driver()


class Pandora:

    def get_trading_pairs(self):
        driver = DriverInitializer('https://pandora.digital/info/tokens', False).initialize_driver()
