from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from org.selenium.base.BaseClass import BaseClass


class HomePage(BaseClass):
    __storeMenuLink = (By.CSS_SELECTOR, "#menu-item-1227")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def NavigateToStoreUsingMenu(self):
        self.clickOnElement(self.__storeMenuLink)
        # return Storepage(self.driver)

    def homePageLoad(self):
        self.load("/")
        self.waitForElement.until(expected_conditions.title_contains("AskOmDch"))
        return HomePage



