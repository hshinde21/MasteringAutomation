from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Base.BasePage import BaseClass
from Utilities import configReader
from pages.CartPage import CartPage


class StorePage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    __searchField = "#woocommerce-product-search-field-0"
    __searchButton = "#woocommerce_product_search-1>form>button"
    __title = ".woocommerce-products-header>h1"
    __viewCartLink = "a[title='View cart']"
    __getAddToCartButtonElement = By.CSS_SELECTOR, "a[aria-label='Add “"

    def IsPageLoaded(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        return wait.until(ec.url_contains(configReader.readConfig("URL", "endpoint")))
        # return wait.until(ec.url_contains(configReader.config("endpoint")))
        print_stack()

    def __enterTextInSearchField(self, text):
        self.sendText(text, self.__searchField, "css")

    def clickSearchButton(self):
        self.clickOnElement(self.__searchButton, "css")
        return self

    def getSearchResultsHeaderTitle(self):
        self.Text(self.__title, "css")

    def getAddToCartButtonElement(self, productName):
        element = self.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Add “" + productName + "” to your cart']")
        element.click()
        # return self.driver.find_css_selector("a[aria-label='Add “" + productName + "” to your cart']")
        # "a[aria-label='Add “" + productName + "” to your cart']"
        # return self.driver.find_element(By.CSS_SELECTOR, "a[title='View cart']").click()

    def clickAddToCartButton(self, productName):
        self.getAddToCartButtonElement(productName)

    def search(self, text):
        self.__enterTextInSearchField(text)
        self.clickSearchButton()

    def clickViewCartLink(self):
        self.clickOnElement(self.__viewCartLink, "css")
        return CartPage(self.driver)
