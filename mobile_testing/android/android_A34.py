import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


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
    sleep(3)
    locator_1 = '//android.widget.Button[@content-desc="Continue"]'
    el_1 = driver.find_element(by=AppiumBy.XPATH, value=locator_1)
    el_1.click()
    sleep(3)
    locator_2 = '//android.widget.Button[@content-desc="Continue"]'
    el_2 = driver.find_element(by=AppiumBy.XPATH, value=locator_2)
    el_2.click()


def login_password(driver):
    password_button = driver.find_elemnent(AppiumBy)

#     locator_3 = 'android.widget.EditText'
#     locator_4 = '//android.widget.ScrollView/android.widget.EditText[2]'
#
#     wait = WebDriverWait(driver, 10)
#
#     password_field = driver.find_element(by=AppiumBy.CLASS_NAME, value=locator_3)
#     password_field_1 = driver.find_element(by=AppiumBy.XPATH, value=locator_4)
#     password_field.click()
#     # Input the password in the first input field
#
#     password_field.click()
#     password_field.send_keys('123456')
#     password_field_1.click()
#     password_field_1.send_keys('123456')
#
#     sleep(5)
#
#
# if __name__ == '__main__':
#     pytest.main()