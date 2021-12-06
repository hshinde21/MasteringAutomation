import pytest

from org.selenium.POM.pages.Homepage import HomePage
from org.selenium.base.BasePage import BasePage
from org.selenium.test.BaseTest import BaseTest



class testCaseOne(BaseTest):



    def test_One(self):
        Home = HomePage(self.driver)
        Home.NavigateToStoreUsingMenu()


test = testCaseOne()
test.test_One()
