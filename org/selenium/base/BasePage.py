# from traceback import print_stack
# import allure
# import duration
# from allure_commons.types import AttachmentType
# from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec, expected_conditions
# import utils.custom_logger as cl
# import logging
#
# from org.selenium.base.DriverManager import DriverManager
#
#
# class Baseass:
#     log = cl.customLogger()
#
#     def __init__(self, driver):
#
#         self.driver = driver
#
#     def waitForElement(self, locatorvalue, locatorType):
#         locatorType = locatorType.lower()
#         element = None
#         wait = WebDriverWait(self.driver, 25, poll_frequency=1,
#
#                              ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
#                                                  NoSuchElementException])
#         if locatorType == "id":
#             element = wait.until(lambda x: x.find_element(By.ID(locatorvalue)))
#             # wait.until(expected_conditions.presence_of_element_located(lambda x: x.find_element(By.CSS_SELECTOR(locatorvalue))))
#             return element
#         elif locatorType == "class":
#             element = wait.until(lambda x: x.find_element(By.CLASS_NAME(locatorvalue)))
#             return element
#         elif locatorType == "xpath":
#             element = wait.until(lambda x: x.find_element(By.XPATH(locatorvalue)))
#             return element
#         elif locatorType == "css":
#             element = wait.until(lambda x: x.find_element(By.CSS_SELECTOR(locatorvalue)))
#             return element
#
#         elif locatorType == "tag":
#             element = wait.until(lambda x: x.find_element(By.TAG_NAME(locatorvalue)))
#             return element
#         elif locatorType == "link":
#             element = wait.until(lambda x: x.find_element(By.LINK_TEXT(locatorvalue)))
#             return element
#
#         elif locatorType == "partiallink":
#             element = wait.until(lambda x: x.find_element(By.PARTIAL_LINK_TEXT(locatorvalue)))
#             return element
#         elif locatorType == "class":
#             element = wait.until(lambda x: x.find_element(By.NAME(locatorvalue)))
#             return element
#         else:
#             self.log.info("Locator value " + locatorvalue + "not found")
#
#         return element
#
#     def getWebElement(self, locatorValue, locatorType="id"):
#         webElement = None
#         try:
#             locatorType = locatorType.lower()
#             locatorByType = self.getLocatorType(locatorType)
#             webElement = self.driver.find_element(locatorByType, locatorValue)
#             self.log.info("WebElement found with locator value " + locatorValue + " using locatorType " + locatorByType)
#         except:
#             self.log.error(
#                 "WebElement not found with locator value " + locatorValue + " using locatorType " + locatorType)
#             print_stack()
#         return webElement
#
#     def waitForElement(self, locatorValue, locatorType="id"):
#         webElement = None
#         try:
#             locatorType = locatorType.lower()
#             locatorByType = self.getLocatorType(locatorType)
#             wait = WebDriverWait(self.driver, 25, poll_frequency=1,
#                                  ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
#             webElement = wait.until(ec.presence_of_element_located((locatorByType, locatorValue)))
#             self.log.info("WebElement found with locator value " + locatorValue + " using locatorType " + locatorType)
#         except:
#             self.log.error(
#                 "WebElement not found with locator value " + locatorValue + " using locatorType " + locatorType)
#             print_stack()
#         return webElement
#
#     def clickOnElement(self, locatorValue, locatorType="id"):
#         try:
#             locatorType = locatorType.lower()
#             webElement = self.waitForElement(locatorValue, locatorType)
#             webElement.click()
#             self.log.info(
#                 "Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
#         except:
#             self.log.error("Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
#             print_stack()
#             assert False
#
#     def sendText(self, text, locatorValue, locatorType="id"):
#         try:
#             locatorType = locatorType.lower()
#             webElement = self.waitForElement(locatorValue, locatorType)
#             webElement.send_keys(text)
#             self.log.info(
#                 "Sent the text " + text + " in WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
#         except:
#             self.log.error(
#                 "Unable to Sent the text " + text + " in WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
#             print_stack()
#
#     def getText(self, locatorValue, locatorType="id"):
#         elementText = None
#         try:
#             locatorType = locatorType.lower()
#             webElement = self.waitForElement(locatorValue, locatorType)
#             elementText = webElement.text
#             self.log.info(
#                 "Got the text " + elementText + " from WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
#         except:
#             self.log.error(
#                 "Unable to get the text " + elementText + " from WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
#             print_stack()
#
#         return elementText
#
#     def isElementDisplayed(self, locatorValue, locatorType="id"):
#         elementDisplayed = None
#         try:
#             locatorType = locatorType.lower()
#             webElement = self.waitForElement(locatorValue, locatorType)
#             elementDisplayed = webElement.is_displayed()
#             self.log.info(
#                 "WebElement is Displayed on web page with locator value " + locatorValue + " using locatorType " + locatorType)
#         except:
#             self.log.error(
#                 "WebElement is not Displayed on web page with locator value " + locatorValue + " using locatorType " + locatorType)
#             print_stack()
#
#         return elementDisplayed
#
#     def scrollTo(self, locatorValue, locatorType="id"):
#         actions = ActionChains(self.driver)
#         try:
#             locatorType = locatorType.lower()
#             webElement = self.waitForElement(locatorValue, locatorType)
#             actions.move_to_element(webElement).perform()
#             self.log.info(
#                 "Scrolled to WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
#         except:
#             self.log.error(
#                 "Unable to scroll to WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
#             print_stack()
#
#     def load(self, endpoint):
#         try:
#             self.driver.get("https://askomdch.com" + endpoint)
#             self.log.info("Page is loaded with the endpoint" + endpoint)
#         except:
#             self.log.error(
#                 "Page fails to load with the endpoint " + endpoint)
#             print_stack()
#
#     def launchWebPage(self, baseURL):
#         try:
#             self.driver.get(baseURL)
#             self.log.info("Webbrowser is laumched")
#         except:
#             self.log.error("Browser fails to intialize")
#
#
#
#
#
#
#
