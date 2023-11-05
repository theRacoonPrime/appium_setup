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
    'appWaitForLaunch': 'false',
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


def test_login(driver):
    driver.implicitly_wait(20)
    locator = '//android.widget.Button[@content-desc="I already have account"]'
    driver.find_element(by=AppiumBy.XPATH, value=locator).click()
    locator_1 = '//android.widget.Button[@content-desc="Continue"]'
    driver.find_element(by=AppiumBy.XPATH, value=locator_1).click()
    locator_2 = '//android.widget.Button[@content-desc="Continue"]'
    driver.find_element(by=AppiumBy.XPATH, value=locator_2).click()
    wait = WebDriverWait(driver, 20)
    locator_3 = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android' \
                '.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android' \
                '.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1] '
    locator_4 = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android' \
                '.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android' \
                '.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2] '
    element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, locator_3)))
    element.click()
    element.send_keys("123456")
    element_1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, locator_4)))
    element_1.click()
    element_1.send_keys("123456")

