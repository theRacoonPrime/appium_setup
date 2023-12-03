import json
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from ..android import (Card_and_Stikers)
from test_helper import( wait_and_click, appium_server_url, wait_for_element,
                         swipe, driver, enter_text_and_hide_keyboard, perform_actions_with_wait, appium_capabilities,
                         load_locators_card, load_locators)


@pytest.fixture
def setup_teardown():
    # Setup code
    yield


@pytest.mark.run(order=1)
def test_scenario_1():
    # Test scenario 1 implementation
    assert True


@pytest.mark.run(order=2)
def test_scenario_2():
    # Test scenario 2 implementation
    assert True


@pytest.mark.run(order=3)
def test_scenario_3():
    # Test scenario 3 implementation
    assert True
