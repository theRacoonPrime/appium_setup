import json
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from ..test_helper import( wait_and_click, appium_server_url, wait_for_element,
                         swipe, driver, enter_text_and_hide_keyboard, perform_actions_with_wait, appium_capabilities,
                         load_locators_card, load_locators)


# Test using the fixtures
@pytest.fixture
def test_landing_botomm(driver, perform_actions_with_wait, load_locators, load_locators_card):
    locators_data = load_locators   # Use it as a fixture, not a function
    locators_data_load = load_locators_card
    driver.implicitly_wait(20)

    actions = [
        # Login to the app with password input

    ]

    perform_actions_with_wait(actions)


@pytest.fixture
def test_landing_botomm_negative(driver, perform_actions_with_wait, load_locators, load_locators_card):
    locators_data = load_locators   # Use it as a fixture, not a function
    locators_data_load = load_locators_card
    driver.implicitly_wait(20)

    actions = [
        # Login to the app with password input

    ]

    perform_actions_with_wait(actions)