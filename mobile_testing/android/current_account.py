import json
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from test_helper import( wait_and_click, appium_server_url, wait_for_element,
                         swipe, driver, enter_text_and_hide_keyboard, perform_actions_with_wait, appium_capabilities,
                         load_locators_card, load_locators)


# Test using the fixtures
@pytest.fixture
def current_account(driver, perform_actions_with_wait, load_locators):
    locators_data = load_locators  # Use it as a fixture, not a function
    driver.implicitly_wait(5)

    actions = [
        {'action': 'wait_and_click', 'locator': load_locators['acc_button']},
        {'action': 'wait_and_click', 'locator': load_locators['new_payment']},
        # {'action': 'wait_and_click', 'locator': load_locators['choose_acc_from']},
        # {'action': 'wait_and_click', 'locator': load_locators['current_acc_usd']},
        {'action': 'wait_and_click', 'locator': load_locators['choose_acc_to_menu']},
        # {'action': 'swipe', 'start_x': 500, 'start_y': 520, 'end_x': 560, 'end_y': 2160, 'duration': 800},
        {'action': 'wait_and_click', 'locator': load_locators['receiver_acc']},
        {'action': 'swipe'},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['amount_field'], 'text': '12'},
        {'action': 'swipe'},
        # {'action': 'wait_and_click', 'locator': load_locators['model_of_payment']},
        # {'action': 'wait_and_click', 'locator': load_locators['choose_model_of_payment']},
        {'action': 'swipe'},
        # {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['reference_field'], 'text': '1ddfew22'},
        {'action': 'wait_and_click', 'locator': load_locators['continue_payment']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': load_locators['pay_button']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['pin_confirm'], 'text': '123456'},
        {'action': 'wait_and_click', 'locator': load_locators['confirm']},
        {'action': 'wait_and_click', 'locator': load_locators['done']},

    ]

    perform_actions_with_wait(actions)


@pytest.fixture
def test_current_account_negative(driver, perform_actions_with_wait, load_locators):
    locators_data = load_locators  # Use it as a fixture, not a function
    driver.implicitly_wait(20)

    actions = [

    ]

    perform_actions_with_wait(actions)
