import pytest
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.options.ios import XCUITestOptions

appium_capabilities = {
    'automationName': 'xcuitest',
    'platformName': 'iOS',
    'udid': '00008110-001865A91411401E',
    'deviceName': 'IPHONE',
    'app': '/Users/andrey/Downloads/yettel-bank.ipa',
}

appium_capabilities = XCUITestOptions().load_capabilities(appium_capabilities)
appium_server_url = 'http://localhost:4723/wd/hub'


@pytest.fixture()
def driver():
    ios_driver = webdriver.Remote(appium_server_url, options=appium_capabilities)
    yield ios_driver
    if ios_driver:
        ios_driver.quit()


@pytest.mark.parametrize("element_locator, element_description", test_data)
def test_example(driver, element_locator, element_description) -> None:
    el = driver.find_element(by=AppiumBy.XPATH, value=element_locator)
    el.click()
    sleep(10)
