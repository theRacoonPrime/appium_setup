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
with open('/Users/andrey/Desktop/appium_setup/mobile_testing/android/test_data.json') as f:
    locators = json.load(f)

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
@pytest.fixture()
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


def perform_actions_with_wait(driver, actions):
    wait = WebDriverWait(driver, 20)

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


def test_account(driver):
    driver.implicitly_wait(20)

    actions = [
        {'action': 'wait_and_click', 'locator': locators['already_have_account']},
        {'action': 'wait_and_click', 'locator': locators['continue_button']},
        {'action': 'wait_and_click', 'locator': locators['continue_button']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators['password_field_1'], 'text': '123456'},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators['password_field_2'], 'text': '123456'},
        {'action': 'wait_and_click', 'locator': locators['continue_button']},
        {'action': 'wait_and_click', 'locator': locators['thanks_button']},
        {'action': 'wait_and_click', 'locator': locators['device_name']},
        {'action': 'wait_and_click', 'locator': locators['go_to_app_button']},
        {'action': 'wait_and_click', 'locator': locators['password_field_general']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators['password_field_general'], 'text': '123456'},
        {'action': 'wait_and_click', 'locator': locators['accept_button']},
        {'action': 'wait_and_click', 'locator': locators['acc_button']},
        {'action': 'wait_and_click', 'locator': locators['new_payment']},
        {'action': 'wait_and_click', 'locator': locators['choose_acc']},
        {'action': 'wait_and_click', 'locator': locators['exit_button']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators['amount_field'], 'text': '123456'},
        {'action': 'wait_and_click', 'locator': locators['exit_button']},
        {'action': 'wait_and_click', 'locator': locators['tree_dot']},
        {'action': 'wait_and_click', 'locator': locators['copy_button']},
        {'action': 'wait_and_click', 'locator': locators['card_button']},
        {'action': 'wait_and_click', 'locator': locators['exit_card_button']},
        {'action': 'wait_and_click', 'locator': locators['payment_limits_button']},
        {'action': 'wait_and_click', 'locator': locators['exit_payment_limit']},
        {'action': 'wait_and_click', 'locator': locators['statement_button']},
        {'action': 'wait_and_click', 'locator': locators['statement_exit_button']},
        {'action': 'wait_and_click', 'locator': locators['balance_information_button']},
        {'action': 'wait_and_click', 'locator': locators['exit_balance_info']},
        {'action': 'wait_and_click', 'locator': locators['account_info_button']},
        {'action': 'wait_and_click', 'locator': locators['exit_accinfo_button']},
        {'action': 'wait_and_click', 'locator': locators['standing_order']},
        {'action': 'wait_and_click', 'locator': locators['exit_button']},
    ]

    perform_actions_with_wait(driver, actions)
