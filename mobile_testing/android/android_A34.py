import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
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


# test function
def test_example(driver) -> None:
    el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="I already have account"]')
    el_1 = driver.find_element(by=AppiumBy.XPATH,
                               value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View')

    el.click()
    sleep(10)


# Test data
test_data = [
    ('//android.widget.Button[@content-desc="I already have account"]', 'Button Element'),
    (
    '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View',
    'FrameLayout Element'),
]


# Parameterized test function
@pytest.mark.parametrize("element_locator, element_description", test_data)
def test_example_with_params(driver, element_locator, element_description) -> None:
    el = driver.find_element(by=AppiumBy.XPATH, value=element_locator)
    el.click()
    sleep(10)
