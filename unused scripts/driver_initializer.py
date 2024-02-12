import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Created: Sunday, July 31, 2022, 2:03:38 PM


class DriverInitializer:

    """ Selenium WebDriver is an automated testing
    framework used for the validation of websites
    (and web applications). It supports popular programming
    languages such as Python, C#, Java, Ruby, and more. """

    def __init__(self, url: str, headless: bool):
        self.__url = url
        self.__headless = headless

    def initialize_driver(self):
        executable_path = pathlib.Path('../chromedriver.exe').absolute().__str__()
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
