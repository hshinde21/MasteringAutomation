import pytest

from org.selenium.base.BasePage import BasePage
from org.selenium.base.DriverManager import DriverManager


@pytest.yield_fixture(scope='function')
def testBeforeClass(request):
    DriverClassObject = DriverManager("chrome")
    driver = DriverClassObject.initializeDriver()
    basePage = BasePage(driver)
    basePage.launchWebPage("https://askomdch.com/")
    print('Before Class')

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.implicitly_wait(5)
    driver.quit()
    print('After Class')
