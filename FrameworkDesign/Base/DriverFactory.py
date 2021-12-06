import json

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import Utilities.CustomLogger as cl
from Utilities import configReader


class WebDriverClass:
    log = cl.customLogger()


    # def getWebDriver(self, browserName):
    #     driver = None
    #
    #     if browserName == "chrome".lower():
    #         driver = webdriver.Chrome(ChromeDriverManager(path="ChromeDrivers").install())
    #     elif browserName == "FireFox".lower():
    #         driver = webdriver.Firefox(GeckoDriverManager(path="FirefoxDriver").install())
    #         driver.maximize_window()
    #         driver.implicitly_wait(10)
    #
    #     return driver

    def getWebDriver(self, browserName):
        driver = None

        if browserName == configReader.readConfig("Browser", "browserName".lower()):
            driver = webdriver.Chrome(ChromeDriverManager(path="ChromeDrivers").install())
        elif browserName == configReader.readConfig("Browser", "browserName".lower()):
            driver = webdriver.Firefox(GeckoDriverManager(path="FirefoxDriver").install())
            driver.maximize_window()
            driver.implicitly_wait(configReader.readConfig("Browser", "wait"))

            


        return driver


