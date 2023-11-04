import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options

# Desired capabilities to specify the Android device and app details
appium_capabilities = {
    'automationName': 'UiAutomator2',  # Use UiAutomator2 for Android automation
    'platformName': 'Android',
    'udid': 'RZCW711MGVY',
    'deviceName': 'A34',  # Example: 'Pixel 4' or 'emulator-5554'
    'app': '/Users/andrey/Downloads/app-development-release (1).apk',
}

appium_capabilities = UiAutomator2Options().load_capabilities(appium_capabilities)
appium_server_url = 'http://localhost:4723/wd/hub'


# Initialize the Appium driver for Android using a fixture
@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=appium_capabilities)
    yield android_driver
    if android_driver:
        android_driver.quit()


def test_click_already_have_account_button(driver) -> None:
    locator = '//android.widget.Button[@content-desc="I already have account"]'
    el = driver.find_element(by=AppiumBy.XPATH, value=locator)
    el.click()
    sleep(10)
    locator_1 = '//android.widget.Button[@content-desc="Continue"]'
    el_1 = driver.find_element(by=AppiumBy.XPATH, value=locator_1)
    el_1.click()
    sleep(10)
    locator_2 = '//android.widget.Button[@content-desc="Continue"]'
    el_2 = driver.find_element(by=AppiumBy.XPATH, value=locator_2)
    el_2.click()

