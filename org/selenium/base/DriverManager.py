from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverManager:

    def initializeDriver(self, browserName):
        """
      Get WebDriver Instance based on the browser configuration

       Returns:
           'WebDriver Instance'
       """
        driver = None

        if browserName == "chrome".lower():
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browserName == "FireFox".lower():
            driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)

        return driver
