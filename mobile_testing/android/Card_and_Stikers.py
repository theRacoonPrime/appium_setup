import json
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from test_helper import( wait_and_click, appium_server_url, wait_for_element, load_locators,
                         swipe, driver, enter_text_and_hide_keyboard)


# Desired capabilities to specify the Android device and app details
@pytest.fixture
def appium_capabilities():
    # Load appium_capabilities from JSON file
    with open('/Users/andrey/Desktop/appium_setup/mobile_testing/android/capabilities.json') as f:
        capabilities = json.load(f)

    # Configure appium_capabilities using UiAutomator2Options
    capabilities = UiAutomator2Options().load_capabilities(capabilities)

    return capabilities


# Fixture for perform_actions_with_wait
@pytest.fixture
def perform_actions_with_wait(driver):
    def perform_actions(actions):
        for action in actions:
            action_type = action.get('action')
            locator = action.get('locator')
            text = action.get('text')

            if action_type == 'wait_and_click':
                wait_and_click(driver, locator)
            elif action_type == 'enter_text_and_hide_keyboard':
                enter_text_and_hide_keyboard(driver, locator, text)
            elif action_type == 'swipe':
                swipe(driver)

            # Add sleep or wait conditions as needed between actions
            sleep(1)

    return perform_actions


# Test using the fixtures
def test_account(driver, perform_actions_with_wait, load_locators):
    locators_data = load_locators  # Use it as a fixture, not a function
    driver.implicitly_wait(10)

    actions = [
        # Login to the app with password input
        {'action': 'wait_and_click', 'locator': locators_data['already_have_account']},
        {'action': 'wait_and_click', 'locator': locators_data['continue_button']},
        {'action': 'wait_and_click', 'locator': locators_data['continue_button']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['password_field_1'], 'text': '123456'},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['password_field_2'], 'text': '123456'},
        {'action': 'wait_and_click', 'locator': locators_data['continue_button']},
        {'action': 'wait_and_click', 'locator': locators_data['thanks_button']},
        {'action': 'wait_and_click', 'locator': locators_data['device_name']},
        {'action': 'wait_and_click', 'locator': locators_data['go_to_app_button']},
        {'action': 'wait_and_click', 'locator': locators_data['password_field_general']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['password_field_general'],'text': '123456'},
        {'action': 'wait_and_click', 'locator': locators_data['accept_button']},
        # Choose acc TO button
        {'action': 'wait_and_click', 'locator': locators_data['show_more']},
        {'action': 'wait_and_click', 'locator': locators_data['acc_button']},
        {'action': 'wait_and_click', 'locator': locators_data['tree_dot']},
        {'action': 'wait_and_click', 'locator': locators_data['card_image']},
        {'action': 'wait_and_click', 'locator': locators_data['card_button_1']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': locators_data['exit_from_card']},
        {'action': 'wait_and_click', 'locator': locators_data['card_button_2']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': locators_data['exit_from_card']},
        {'action': 'wait_and_click', 'locator': locators_data['card_button_3']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': locators_data['exit_from_card']},
        {'action': 'wait_and_click', 'locator': locators_data['card_button_4']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_from_card']},
        {'action': 'wait_and_click', 'locator': locators_data['card_button_5']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_from_card']},
        {'action': 'wait_and_click', 'locator': locators_data['card_button_6']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_from_card']},
    ]

    perform_actions_with_wait(actions)
