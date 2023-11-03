import pytest
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.options.android import UiAutomator2Options


appium_capabilities = {
    'automationName': 'UiAutomator2',  # Use UiAutomator2 for Android automation
    'platformName': 'Android',
    'udid': 'RZCW711MGVY',
    'deviceName': 'A34',  # Example: 'Pixel 4' or 'emulator-5554'
    'app': '/Users/andrey/Downloads/app-development-release (1).apk',
}

appium_capabilities = UiAutomator2Options().load_capabilities(appium_capabilities)
appium_server_url = 'http://localhost:4723/wd/hub'
# Initialize the Appium driver for Android


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=appium_capabilities)
    yield android_driver
    if android_driver:
        android_driver.quit()


# def test_example(driver) -> None:
#     el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="I already have account"]')
#     el_1 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View')
#     # el_2 = driver.find_element(by=AppiumBy.ID, value='00000000-0000-051b-0000-003c00000004')
#     # el_3 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]')
#     el.click()
#     # el_1.click()
#     # el_2.click()
#     # el_3.click()
#     sleep(10)


test_data = [
    ('//android.widget.Button[@content-desc="I already have account"]', 'Button Element'),
    ('//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View', 'FrameLayout Element'),
]


@pytest.mark.parametrize("element_locator, element_description", test_data)
def test_example(driver, element_locator, element_description) -> None:
    el = driver.find_element(by=AppiumBy.XPATH, value=element_locator)
    el.click()
    sleep(10)


