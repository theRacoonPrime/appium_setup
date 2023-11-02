import pytest
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver as selenium_webdriver

# Define the test data as a list of search queries
search_queries = ["Appium", "Mobile Testing", "Automation"]


@pytest.fixture(scope="function")       # First fixture
def appium_driver():
    # Short describe of capabilities
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': 'A34',
        'automationName': 'UiAutomator2',
        'app': '/Users/andrey/Downloads/app-development-release (1).apk',
        'udid': "RZCW711MGVY",  # Must be change for your UDID for ANDROID
        "noReset": "true"
    }

    # Start the Appium driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    yield driver
    driver.quit()


@pytest.mark.parametrize("search_query", search_queries)        # Parametrise decorator
def test_search_and_click_button(appium_driver, search_query):
    # Find the "I already have account" button using the specified XPath
    already_have_account_button = appium_driver.find_element(
        AppiumBy.XPATH, '//android.widget.Button[@content-desc="I already have account"]'
    )
    already_have_account_button.click()

    # Close the app
    appium_driver.close_app()

