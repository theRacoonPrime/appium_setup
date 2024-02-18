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
from test_helper import (wait_and_click, appium_server_url, wait_for_element, load_locators,
                         swipe, driver, enter_text_and_hide_keyboard, perform_actions_with_wait, appium_capabilities,
                         wait_fun, landing_page, settings_load)


@pytest.fixture
def test_settings(driver, perform_actions_with_wait, load_locators, settings_load):
    locators_data = load_locators
    settings = settings_load  # Use it as a fixture, not a function
    driver.implicitly_wait(5)

    # Add a sleep time before the test actions
    sleep_time_before_actions = 0  # Adjust the duration as needed
    time.sleep(sleep_time_before_actions)

    actions = [
        # Login to the app with password input
        {'action': 'wait_and_click', 'locator': locators_data['already_have_account']},
        {'action': 'wait_and_click', 'locator': locators_data['continue_button']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['Sms_code_button'], 'text': '111111'},
        {'action': 'wait_and_click', 'locator': locators_data['continue_button']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['password_field_1'], 'text': '123456'},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['password_field_2'], 'text': '123456'},
        {'action': 'wait_and_click', 'locator': locators_data['continue_button']},
        {'action': 'wait_and_click', 'locator': locators_data['thanks_button']},
        {'action': 'wait_and_click', 'locator': locators_data['confirm_button']},
        {'action': 'wait_and_click', 'locator': locators_data['device_name']},
        {'action': 'wait_and_click', 'locator': locators_data['go_to_app_button']},
        {'action': 'wait_and_click', 'locator': settings_load['menu_button']},
        {'action': 'wait_and_click', 'locator': settings_load['change_packages']},
        {'action': 'wait_and_click', 'locator': settings_load['exit_form_packages']},
        {'action': 'wait_and_click', 'locator': settings_load['payments_button']},
        {'action': 'wait_and_click', 'locator': settings_load['exit_payments']},
        {'action': 'wait_and_click', 'locator': settings_load['exchange_office']},
        {'action': 'wait_and_click', 'locator': settings_load['exit_from_exchange']},
        {'action': 'wait_and_click', 'locator': settings_load['standing_order']},
        {'action': 'wait_and_click', 'locator': settings_load['exit_from_standing_order']},
        {'action': 'wait_and_click', 'locator': settings_load['card_overview']},
        {'action': 'wait_and_click', 'locator': settings_load['exit_from_card_overview']},
        {'action': 'wait_and_click', 'locator': settings_load['transaction_overview']},
        {'action': 'wait_and_click', 'locator': settings_load['exit_from_transactions']},
        {'action': 'wait_and_click', 'locator': settings_load['account_details']},
        {'action': 'wait_and_click', 'locator': settings_load['exit_from_acc_details']},
        {'action': 'wait_and_click', 'locator': settings_load['statements']},
        {'action': 'wait_and_click', 'locator': settings_load['exit_statements']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': settings_load['settings']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': settings_load['exit_from_settings']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': settings_load['my_profile']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': settings_load['exit_from_my_profile']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': settings_load['limits']},
        {'action': 'wait_and_click', 'locator': settings_load['exit_from_limits']},
        {'action': 'wait_and_click', 'locator': settings_load['Contact_us']},
        {'action': 'wait_and_click', 'locator': settings_load['Contact_US_exit']},
        {'action': 'swipe'},
        {'action': 'wait_and_click', 'locator': settings_load['General_inquiry']},
        {'action': 'wait_and_click', 'locator': settings_load['General_inquiry_exit']},
        {'action': 'wait_and_click', 'locator': settings_load['Complaints']},
        {'action': 'wait_and_click', 'locator': settings_load['Complaints_exit']},
        {'action': 'wait_and_click', 'locator': settings_load['FAQ']},
        {'action': 'wait_and_click', 'locator': settings_load['Exit_From_FAQ']},
        {'action': 'wait_and_click', 'locator': settings_load['About_Yettel']},
        {'action': 'wait_and_click', 'locator': settings_load['Exit_About_Yettel']},
    ]

    perform_actions_with_wait(actions)

