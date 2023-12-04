import json
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from test_helper import( wait_and_click, appium_server_url, wait_for_element,
                         swipe, driver, enter_text_and_hide_keyboard, perform_actions_with_wait, appium_capabilities,
                         load_locators_card, load_locators)


# Test using the fixtures
@pytest.fixture
def test_cards(driver, perform_actions_with_wait, load_locators, load_locators_card):
    locators_data = load_locators   # Use it as a fixture, not a function
    locators_data_load = load_locators_card
    driver.implicitly_wait(20)

    actions = [
        # # Login to the app with password input
        # {'action': 'wait_and_click', 'locator': locators_data['already_have_account']},
        # {'action': 'wait_and_click', 'locator': locators_data['continue_button']},
        # {'action': 'wait_and_click', 'locator': locators_data['continue_button']},
        # {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['password_field_1'], 'text': '123456'},
        # {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['password_field_2'], 'text': '123456'},
        # {'action': 'wait_and_click', 'locator': locators_data['continue_button']},
        # {'action': 'wait_and_click', 'locator': locators_data['thanks_button']},
        # {'action': 'wait_and_click', 'locator': locators_data['device_name']},
        # {'action': 'wait_and_click', 'locator': locators_data['go_to_app_button']},
        # {'action': 'wait_and_click', 'locator': locators_data['password_field_general']},
        # {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['password_field_general'],'text': '123456'},
        # {'action': 'wait_and_click', 'locator': locators_data['accept_button']},
        # Choose acc TO button
        {'action': 'wait_and_click', 'locator': locators_data['show_more']},
        {'action': 'wait_and_click', 'locator': locators_data_load['acc_button']},
        {'action': 'wait_and_click', 'locator': locators_data_load['tree_dot']},
        {'action': 'wait_and_click', 'locator': locators_data_load['card_image']},
        {'action': 'wait_and_click', 'locator': locators_data_load['card_button_1']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': locators_data_load['exit_from_card']},
        {'action': 'wait_and_click', 'locator': locators_data_load['card_button_2']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': locators_data_load['exit_from_card']},
        {'action': 'wait_and_click', 'locator': locators_data_load['card_button_3']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': locators_data_load['exit_from_card']},
        {'action': 'wait_and_click', 'locator': locators_data_load['card_button_4']},
        {'action': 'wait_and_click', 'locator': locators_data_load['exit_from_card']},
        {'action': 'wait_and_click', 'locator': locators_data_load['card_button_5']},
        {'action': 'wait_and_click', 'locator': locators_data_load['exit_from_card']},
        {'action': 'wait_and_click', 'locator': locators_data_load['card_button_6']},
        {'action': 'wait_and_click', 'locator': locators_data_load['exit_from_card']},
    ]

    perform_actions_with_wait(actions)
