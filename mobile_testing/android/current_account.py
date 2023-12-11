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
    driver.implicitly_wait(20)

    actions = [
        {'action': 'wait_and_click', 'locator': locators_data['acc_button']},
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
        # Standing order
        {'action': 'wait_and_click', 'locator': locators_data['standing_order_chose']},
        {'action': 'wait_and_click', 'locator': locators_data['acc_from_standing_order']},
        {'action': 'wait_and_click', 'locator': locators_data['acc_from_standing_order_chose']},
        {'action': 'wait_and_click', 'locator': locators_data['standing_order_from_acc_chose']},
        {'action': 'wait_and_click', 'locator': locators_data['acc_from_standing_order_choose']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['amount_field_standing_order'], 'text': '123'},
        {'action': 'swipe'},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['standing_order_nickname_filed'],
         'text': 'blabla'},
        {'action': 'wait_and_click', 'locator': locators_data['continue_choose_menu']},
        {'action': 'wait_and_click', 'locator': locators_data['confirm_choose_menu']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_button']},
    ]

    perform_actions_with_wait(actions)

