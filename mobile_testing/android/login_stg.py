import json
import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from test_helper import( wait_and_click, appium_server_url, wait_for_element, load_locators,
                         swipe, driver, enter_text_and_hide_keyboard, perform_actions_with_wait, appium_capabilities,
                         wait_fun, user_data_load)


@pytest.fixture
def test_login_stg(driver, perform_actions_with_wait, load_locators, user_data_load):
    locators_data = load_locators
    user_data_load = user_data_load  # Use it as a fixture, not a function
    driver.implicitly_wait(5)

    # Add a sleep time before the test actions
    sleep_time_before_actions = 0  # Adjust the duration as needed
    time.sleep(sleep_time_before_actions)

    actions = [
        {'action': 'wait_and_click', 'locator': user_data_load['account']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': user_data_load['number_phone'], 'text': '38118823339'},
        {'action': 'enter_text_and_hide_keyboard', 'locator': user_data_load['digit_number'], 'text': '4116'},
        # {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['Sms_code_button'], 'text': '111111'},
        # {'action': 'wait_and_click', 'locator': locators_data['continue_button']},
        # {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['password_field_1'], 'text': '123456'},
        # {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['password_field_2'], 'text': '123456'},
     ]

    perform_actions_with_wait(actions)