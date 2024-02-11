import json
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from test_helper import (wait_and_click, appium_server_url, wait_for_element,
                         swipe, driver, enter_text_and_hide_keyboard, perform_actions_with_wait, appium_capabilities,
                         load_locators_card, load_locators)


# Test using the fixtures
@pytest.fixture
def test_cards(driver, perform_actions_with_wait, load_locators, load_locators_card):
    locators_data = load_locators  # Use it as a fixture, not a function
    locators_data_load = load_locators_card
    driver.implicitly_wait(20)

    actions = [
        {'action': 'wait_and_click', 'locator': locators_data_load['card_image']},
        {'action': 'wait_and_click', 'locator': locators_data_load['card_button_1']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': locators_data_load['pencil_button_1']},
        {'action': 'wait_and_click', 'locator': locators_data_load['confirm_button']},
        {'action': 'wait_and_click', 'locator': locators_data_load['exit_from_card']},
        # {'action': 'swipe', 'start_x': 500, 'start_y': 520, 'end_x': 560, 'end_y': 2160, 'duration': 800},
        {'action': 'wait_and_click', 'locator': locators_data_load['card_button_2']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': locators_data_load['pencil_button_2']},
        {'action': 'wait_and_click', 'locator': locators_data_load['confirm_button']},
        {'action': 'wait_and_click', 'locator': locators_data_load['exit_from_card']},
        {'action': 'wait_and_click', 'locator': locators_data_load['card_button_3']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': locators_data_load['exit_from_card']},
        {'action': 'wait_and_click', 'locator': locators_data_load['card_button_4']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': locators_data_load['exit_from_card']},
        # {'action': 'wait_and_click', 'locator': locators_data_load['card_button_5']},
        # {'action': 'swipe'},
        # {'action': 'wait_and_click', 'locator': locators_data_load['exit_from_card']},
        # {'action': 'wait_and_click', 'locator': locators_data_load['card_button_6']},
        # {'action': 'swipe'},
        # {'action': 'wait_and_click', 'locator': locators_data_load['exit_from_card']},
    ]

    perform_actions_with_wait(actions)


@pytest.fixture
def test_cards_negative(driver, perform_actions_with_wait, load_locators, load_locators_card):
    locators_data = load_locators  # Use it as a fixture, not a function
    locators_data_load = load_locators_card
    driver.implicitly_wait(20)

    actions = [
        # Choose acc TO button
    ]

    perform_actions_with_wait(actions)
