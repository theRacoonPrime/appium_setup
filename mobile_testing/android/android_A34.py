import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput

# Desired capabilities to specify the Android device and app details
appium_capabilities = {
    'automationName': 'UiAutomator2',  # Use UiAutomator2 for Android automation
    'platformName': 'Android',
    'udid': 'RZCW711MGVY',
    'deviceName': 'A34',  # Example: 'Pixel 4' or 'emulator-5554'
    'app': '/Users/andrey/Downloads/app-development-release (1).apk',
    'appWaitForLaunch': 'false',
}

appium_capabilities = UiAutomator2Options().load_capabilities(appium_capabilities)
appium_server_url = 'http://localhost:4723/wd/hub'


# Initialize the Appium driver for Android using a fixture
@pytest.fixture()
def driver():
    android_driver = webdriver.Remote('http://localhost:4723/wd/hub', options=appium_capabilities)
    yield android_driver
    if android_driver:
        android_driver.quit()


# Common actions
def click_element(driver, locator):
    element = driver.find_element(by=AppiumBy.XPATH, value=locator)
    element.click()


def enter_text(driver, locator, text):
    element = driver.find_element(by=AppiumBy.XPATH, value=locator)
    element.click()
    element.send_keys(text)


# Test data

locators = {
    'already_have_account': '//android.widget.Button[@content-desc="I already have account"]',
    'continue_button': '//android.widget.Button[@content-desc="Continue"]',
    'password_field_1': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout'
                        '/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android'
                        '.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]',
    'password_field_2': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout'
                        '/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android'
                        '.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]',
    'accept_button': '//android.widget.Button[@content-desc="Accept"]',
    'thanks_button': '//android.widget.Button[@content-desc="Thanks, but not now"]',
    'go_to_app_button': '//android.widget.Button[@content-desc="Go to the app"]',
    'password_field_general': '//android.widget.EditText',
}


# Test functions
def test_login(driver):
    driver.implicitly_wait(20)

    click_element(driver, locators['already_have_account'])
    click_element(driver, locators['continue_button'])
    click_element(driver, locators['continue_button'])

    wait = WebDriverWait(driver, 20)

    enter_text(driver, locators['password_field_1'], '123456')
    enter_text(driver, locators['password_field_2'], '123456')

    click_element(driver, locators['continue_button'])
    click_element(driver, locators['thanks_button'])
    click_element(driver, locators['go_to_app_button'])

    enter_text(driver, locators['password_field_general'], '123456')

    click_element(driver, locators['accept_button'])

    sleep(20)
