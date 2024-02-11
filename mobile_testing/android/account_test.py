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
def payment(driver, perform_actions_with_wait, load_locators):
    locators_data = load_locators  # Use it as a fixture, not a function
    driver.implicitly_wait(5)

    actions = [
        {'action': 'wait_and_click', 'locator': load_locators['acc_button']},
        {'action': 'wait_and_click', 'locator': load_locators['tree_dot']},
        {'action': 'wait_and_click', 'locator': load_locators['payment_limits_button']},
        {'action': 'wait_and_click', 'locator': load_locators['exit_payment_limit']},
        {'action': 'wait_and_click', 'locator': load_locators['statement_button']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': load_locators['statement_exit_button']},
        # {'action': 'swipe', 'start_x': 500, 'start_y': 520, 'end_x': 560, 'end_y': 2160, 'duration': 800},
        {'action': 'wait_and_click', 'locator': load_locators['balance_information_button']},
        {'action': 'wait_and_click', 'locator': load_locators['exit_balance_info']},
        {'action': 'wait_and_click', 'locator': load_locators['account_info_button']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': load_locators['exit_accinfo_button']},
        {'action': 'wait_and_click', 'locator': load_locators['standing_order']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': load_locators['exit_from_standing_order']},
        {'action': 'wait_and_click', 'locator': load_locators['copy_button']},
    ]
    perform_actions_with_wait(actions)


@pytest.fixture
def payment_negative_test(driver, perform_actions_with_wait, load_locators):
    locators_data = load_locators  # Use it as a fixture, not a function
    driver.implicitly_wait(20)

    actions = [
    ]

    perform_actions_with_wait(actions)