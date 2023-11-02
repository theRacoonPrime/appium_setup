import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

# Define the test data as a list of search queries
search_queries = ["Appium", "Mobile Testing", "Automation"]


@pytest.fixture(scope="function")
def appium_driver():
    # Desired capabilities for the Android device and app
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': 'A34',
        'automationName': 'UiAutomator2',
        'app': '/Users/andrey/Downloads/app-development-release (1).apk',
    }

    # Initialize the Appium driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    yield driver
    driver.quit()


@pytest.mark.parametrize("search_query", search_queries)
def test_search(appium_driver, search_query):
    # Find and interact with elements in the app
    search_field = appium_driver.find_element(MobileBy.ID, 'com.example.app:id/search_field')
    search_field.send_keys(search_query)

    search_button = appium_driver.find_element(MobileBy.ID, 'com.example.app:id/search_button')
    search_button.click()

    # # Perform a swipe on the screen
    # action = TouchAction(appium_driver)
    # action.press(x=500, y=1500).move_to(x=500, y=500).release().perform()

    # Close the app
    appium_driver.close_app()
