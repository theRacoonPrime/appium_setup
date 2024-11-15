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
                         wait_fun,landing_page)


@pytest.fixture
def test_landing_page(driver, perform_actions_with_wait, load_locators, landing_page):
    locators_data = load_locators
    landing_page = landing_page    # Use it as a fixture, not a function
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
        {'action': 'wait_and_click', 'locator': locators_data['menu_button']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_from_settings_button']},
        {'action': 'wait_and_click', 'locator': landing_page['chat_button']},
        {'action': 'wait_and_click', 'locator': landing_page['exit_from_chat']},
        {'action': 'wait_and_click', 'locator': landing_page['rate_button']},
        {'action': 'wait_and_click', 'locator': landing_page['exit_from_rate_button']},
        {'action': 'wait_and_click', 'locator': landing_page['IPS']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': landing_page['ips_confirm'], 'text': '123456'},
        {'action': 'wait_and_click', 'locator': landing_page['Confirm_button']},
        {'action': 'wait_and_click', 'locator': landing_page['exit_from_IPS']},
        {'action': 'wait_and_click', 'locator': landing_page['locations_button']},
        {'action': 'wait_and_click', 'locator': landing_page['exit_from_locations_button']},
        {'action': 'wait_and_click', 'locator': landing_page['hamburger']},
        {'action': 'wait_and_click', 'locator': landing_page['Contacts']},
        {'action': 'wait_and_click', 'locator': landing_page['Exit_from_contacts']},
        {'action': 'wait_and_click', 'locator': landing_page['hamburger']},
        {'action': 'wait_and_click', 'locator': landing_page['Locations']},
        {'action': 'wait_and_click', 'locator': landing_page['Exit_from_Locations']},
        {'action': 'wait_and_click', 'locator': landing_page['hamburger']},
        {'action': 'wait_and_click', 'locator': landing_page['Currency']},
        {'action': 'wait_and_click', 'locator': landing_page['exit_from_Currency']},
        {'action': 'wait_and_click', 'locator': landing_page['hamburger']},
        {'action': 'wait_and_click', 'locator': landing_page['About app']},
        {'action': 'wait_and_click', 'locator': landing_page['Exit_from_AboutAPP']},
        {'action': 'wait_and_click', 'locator': landing_page['hamburger']},
        {'action': 'wait_and_click', 'locator': landing_page['Yettel']},
        {'action': 'wait_and_click', 'locator': landing_page['Exit_from_AboutYettel']},

     ]

    perform_actions_with_wait(actions)
