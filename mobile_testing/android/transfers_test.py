import json
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from test_helper import( wait_and_click, appium_server_url,
                         wait_for_element,
                         swipe, driver, enter_text_and_hide_keyboard,
                         perform_actions_with_wait,
                         appium_capabilities,
                         load_locators_card, load_locators)


# Test using the fixtures
def test_account(driver, perform_actions_with_wait, load_locators):
    locators_data = load_locators  # Use it as a fixture, not a function
    driver.implicitly_wait(20)

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
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['password_field_general'], 'text': '123456'},
        {'action': 'wait_and_click', 'locator': locators_data['accept_button']},
        {'action': 'wait_and_click', 'locator': locators_data['acc_button']},
        {'action': 'wait_and_click', 'locator': locators_data['new_payment']},
        # New payment was clicked
        # Choose acc from button
        {'action': 'wait_and_click', 'locator': locators_data['choose_acc_from']},
        {'action': 'wait_and_click', 'locator': locators_data['current_acc_rsd']},
        # # Choose acc TO button
        {'action': 'wait_and_click', 'locator': locators_data['choose_acc_to_menu']},
        {'action': 'wait_and_click', 'locator': locators_data['saving_acc_choose_menu']},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['amount_field'], 'text': '123'},
        {'action': 'wait_and_click', 'locator': locators_data['data_choose_menu']},
        {'action': 'wait_and_click', 'locator': locators_data['quarterly_choose_menu']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_choose_menu']},
        {'action': 'swipe'},
        {'action': 'enter_text_and_hide_keyboard', 'locator': locators_data['standing_order_choose_menu'], 'text': '123'},
        {'action': 'wait_and_click', 'locator': locators_data['continue_choose_menu']},
        {'action': 'wait_and_click', 'locator': locators_data['confirm_choose_menu']},
        {'action': 'wait_and_click', 'locator': locators_data['done_button_choose_menu']},
        {'action': 'wait_and_click', 'locator': locators_data['exit_button']},
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