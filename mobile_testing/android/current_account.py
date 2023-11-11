import json
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput


# Load locators from JSON file
@pytest.fixture
def load_locators():
    with open('/Users/andrey/Desktop/appium_setup/mobile_testing/android/test_data.json') as f:
        return json.load(f)

# Desired capabilities to specify the Android device and app details
appium_capabilities = {
    'automationName': 'UiAutomator2',
    'platformName': 'Android',
    'udid': 'RZCW711MGVY',
    'deviceName': 'A34',
    'app': '/Users/andrey/Downloads/app-development-release (2).apk',
    'appWaitForLaunch': 'false',
    'autoGrantPermissions': True,  # It is important to avoid android notification
}

appium_capabilities = UiAutomator2Options().load_capabilities(appium_capabilities)
appium_server_url = 'http://localhost:4723/wd/hub'

# Initialize the Appium driver for Android using a fixture
@pytest.fixture
def driver():
    android_driver = webdriver.Remote('http://localhost:4723/wd/hub', options=appium_capabilities)
    yield android_driver
    if android_driver:
        android_driver.quit()

# Common actions
def wait_and_click(driver, locator):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
    element.click()

def enter_text_and_hide_keyboard(driver, locator, text):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
    element.click()
    element.send_keys(text)
    driver.hide_keyboard()

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

            # Add sleep or wait conditions as needed between actions
            sleep(1)

    return perform_actions


# Test using the fixtures
def test_account(driver, perform_actions_with_wait, load_locators):
    locators_data = load_locators  # Use it as a fixture, not a function
    driver.implicitly_wait(20)

    actions = [
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
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['password_field_general'], 'text': '123456'},
        {'action': 'wait_and_click', 'locator': locators_data['accept_button']},
        {'action': 'wait_and_click', 'locator': locators_data['acc_button']},
        {'action': 'wait_and_click', 'locator': locators_data['new_payment']},
        {'action': 'wait_and_click', 'locator': locators_data['choose_acc']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_button']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['amount_field'], 'text': '123456'},
        {'action': 'wait_and_click', 'locator': locators_data['exit_button']},
        {'action': 'wait_and_click', 'locator': locators_data['tree_dot']},
        {'action': 'wait_and_click', 'locator': locators_data['copy_button']},
        {'action': 'wait_and_click', 'locator': locators_data['card_button']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_card_button']},
        {'action': 'wait_and_click', 'locator': locators_data['payment_limits_button']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_payment_limit']},
        {'action': 'wait_and_click', 'locator': locators_data['statement_button']},
        {'action': 'wait_and_click', 'locator': locators_data['statement_exit_button']},
        {'action': 'wait_and_click', 'locator': locators_data['balance_information_button']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_balance_info']},
        {'action': 'wait_and_click', 'locator': locators_data['account_info_button']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_accinfo_button']},
        {'action': 'wait_and_click', 'locator': locators_data['standing_order']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_button']},
    ]

    perform_actions_with_wait(actions)
