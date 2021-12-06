import json

import allure
import pytest
from allure_commons.types import AttachmentType

from Base.BasePage import BaseClass
from Base.DriverFactory import WebDriverClass
from Utilities import configReader
from Utilities.configReader import config


@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    _driver = WebDriverClass()
    driver = _driver.getWebDriver(configReader.readConfig("Browser", "browserName"))
    baseClass = BaseClass(driver)
    baseClass.launchWebPage(configReader.readConfig("URL", "url"))
    driver.maximize_window()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.implicitly_wait(10)
    driver.quit()
    print('After Class')


@pytest.fixture()
def log_on_failure(request, beforeClass):
    yield
    item = request.node
    driver = beforeClass
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
