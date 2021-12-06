import json
from timeit import time

import jsonpickle
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest

from webdriver_manager.utils import ChromeType


import json

from org.selenium.POM.objects.billingAdress import billingAddress


class MyFirstTest:

    def LoginCheckOutUsingDirectBankTransfer(self):
        """Deserializing the JSON"""
        with open("MybillingAdress.json", "r") as file:
            billing_dict = json.load(file)
            myBillingAddress = billingAddress(billing_dict['firstName'], billing_dict['last_Name'],
                                              billing_dict['company_Name'], billing_dict['Address'], billing_dict['City'],
                                              billing_dict['ZipCode'], billing_dict['Email'])

            billAddressFName = myBillingAddress.setFirstName_In_Billing_Address()
            billAddressLName = myBillingAddress.setLastName_In_Billing_Address()
            billAddressCompanyName = myBillingAddress.setCompanyName_In_Billing_Address()
            billAddressField = myBillingAddress.setAddress_In_Billing_Address()
            biliAddressCityName = myBillingAddress.setCityName_In_Billing_Address()
            billingAddressZip = myBillingAddress.setZipCode_In_Billing_Address()
            billingAddressEmail = myBillingAddress.setEmail_In_Billing_Address()

            baseURL = "https://askomdch.com"
            driver = webdriver.Chrome(ChromeDriverManager(path="Drivers").install())
            # driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM(""))
            driver.get(baseURL)
            driver.maximize_window()

            # driver.find_element_by_css_selector("#menu-item-1227").click()
            driver.find_element(By.CSS_SELECTOR, "#menu-item-1227").click()
            driver.implicitly_wait(10)
            driver.find_element_by_css_selector("#woocommerce-product-search-field-0").send_keys("Blue")
            driver.find_element_by_css_selector("#woocommerce_product_search-1>form>button").click()
            # driver.find_element(By.CSS_SELECTOR("#woocommerce_product_search-1>form>button")).click()
            Text = driver.find_element_by_css_selector(".woocommerce-products-header>h1").text
            print(Text)

            time.sleep(3)
            assert Text in "Search results: “Blue”"

            driver.find_element_by_css_selector("a[aria-label='Add “Blue Shoes” to your cart']").click()
            time.sleep(10)
            driver.find_element(By.CSS_SELECTOR, "a[title='View cart']").click()
            driver.find_element(By.CSS_SELECTOR, ".checkout-button").click()
            driver.find_element(By.CSS_SELECTOR, "#billing_first_name").send_keys(billAddressFName)
            driver.find_element(By.CSS_SELECTOR, "#billing_last_name").send_keys(billAddressLName)
            driver.find_element(By.CSS_SELECTOR, "#billing_company").send_keys(billAddressCompanyName)
            driver.find_element(By.CSS_SELECTOR, "#billing_address_1").send_keys(billAddressField)
            driver.find_element(By.ID, "billing_city").send_keys(biliAddressCityName)
            driver.find_element(By.CSS_SELECTOR,"#billing_postcode").send_keys(billingAddressZip)
            driver.find_element(By.CSS_SELECTOR, "#billing_email").send_keys(billingAddressEmail)
            driver.find_element(By.ID, "place_order").click()
            time.sleep(7)
            print("Last_name entered")
            driver.close()


# driver.findElement(By.cssSelector("#billing_first_name")).sendKeys("Demo");
# driver.findElement(By.cssSelector("#billing_last_name")).sendKeys("user");
chrome = MyFirstTest()
chrome.LoginCheckOutUsingDirectBankTransfer()
