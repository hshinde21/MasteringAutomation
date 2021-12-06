from selenium.webdriver.common.by import By

from Base.BasePage import BaseClass
from pages.StorePage import StorePage


class HomePage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    __storeMenuLink = "#menu-item-1227"

    def NavigateToStoreUsingMenu(self):
        self.clickOnElement(self.__storeMenuLink, "css")
        return StorePage(self.driver)

    """Method to check whether the page is loaded or not"""
    def homePageLoad(self):
        self.load("/")
        self.titleContains("AskOmDch")
        return HomePage
