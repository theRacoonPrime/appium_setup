import json
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from test_helper import( wait_and_click, appium_server_url, wait_for_element, load_locators,
                         swipe, driver, enter_text_and_hide_keyboard, perform_actions_with_wait, appium_capabilities)


# Test using the fixtures
@pytest.fixture
def test_activities_filters(driver, perform_actions_with_wait, load_locators):
    locators_data = load_locators  # Use it as a fixture, not a function
    driver.implicitly_wait(20)

    actions = [

    ]

    perform_actions_with_wait(actions)


@pytest.fixture
def test_activities_filters_negative(driver, perform_actions_with_wait, load_locators):
    locators_data = load_locators  # Use it as a fixture, not a function
    driver.implicitly_wait(20)

    actions = [

    ]

    perform_actions_with_wait(actions)