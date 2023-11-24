# locators.py
import pytest
import json


# Load locators from JSON file
@pytest.fixture
def load_locators():
    with open('/Users/andrey/Desktop/appium_setup/mobile_testing/android/test_data.json') as f:
        return json.load(f)


@pytest.fixture
def load_locator():
    with open('/Users/andrey/Desktop/appium_setup/mobile_testing/android/card_and_stikcers_data.json') as f:
        return json.load(f)


# Define locators_data as a dictionary
locators_data = {
    'already_have_account': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="I already have account"]'},
    'continue_button': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Continue"]'},
    'password_field_1': {'action': 'enter_text_and_hide_keyboard', 'locator': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]'},
    'password_field_2': {'action': 'enter_text_and_hide_keyboard', 'locator': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]'},
    'accept_button': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Accept"]'},
    'thanks_button': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Thanks, but not now"]'},
    'go_to_app_button': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Go to the app"]'},
    'password_field_general': {'action': 'wait_and_click', 'locator': '//android.widget.EditText'},
    'device_name': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Continue"]'},
    'show_more': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Show more"]'},
    'card_image': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Cards"]'},
    'acc_button': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="ten s kartou\n200,00\nRSD"]'},
    'tree_dot': {'action': 'wait_and_click', 'locator': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]'},
    'card_button_1': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Mery\nPetar Petrovic\n12** **** **** **56\n02/2030\nactive"]/android.widget.ImageView[1]'},
    'card_button_2': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Gandalf\nAndrew Enterweder\n12** **** **** **56\n02/2030\nactive"]'},
    'card_button_3': {'action': 'wait_and_click', 'locator': '//android.widget.ImageView[@content-desc="Anton\nAnton Petrovic\n12** **** **** **56 -2\n02/2028\ninactive"]'},
    'card_button_4': {'action': 'wait_and_click', 'locator': '//android.widget.ImageView[@content-desc="Anton\nAnton Petrovic\n12** **** **** **56 -3\n02/2028\npermanently blocked"]'},
    'card_button_5': {'action': 'wait_and_click', 'locator': '//android.widget.ImageView[@content-desc="Anton\nAnton Petrovic\n12** **** **** **56 -4\n02/2028\npermanently blocked"]'},
    'card_button_6': {'action': 'wait_and_click', 'locator': '//android.widget.ImageView[@content-desc="Anton\nAnton Petrovic\n12** **** **** **56 -5\n02/2028\ntemporarily blocked"]'},
    'exit_from_card': {'action': 'wait_and_click', 'locator': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]'},
    'exit_button_from_card_page': {'action': 'wait_and_click', 'locator': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]'},
    'exit_button_from_card_page': {'action': 'wait_and_click', 'locator': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]'},
    'payment_limits_button': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Payment Limits"]'},
    'statement_button': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Statements"]'},
    'balance_information_button': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Balance information"]'},
    'account_info_button': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Account information"]'},
    'standing_order_button': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Standing order"]'},
    'exit_payment_limit': {'action': 'wait_and_click', 'locator': '//android.widget.Button'},
    'statement_exit_button': {'action': 'wait_and_click', 'locator': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]'},
    'acc_info_button': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Balance information"]'},
    'exit_accinfo_button': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Scrim"]'},
    'exit_balance_info': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Scrim"]'},
    'standing_order': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Standing order"]'},
    'exit_button': {'action': 'wait_and_click', 'locator': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'},
    'current_acc_rsd': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="ten s kartou\n00210102101\n200,00\nRSD"]'},
    'current_acc_usd': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Current account 4\n00210102212\n800,00\nRSD"]'},
    'current_acc_eu': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Authorized account 3 700.00 EUR 0898528798"]'},
    'new_payment': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="New payment"]'},
    'amount_field': {'action': 'wait_and_click', 'locator': '//android.widget.EditText'},
    'choose_acc_from': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Current account 4\n00210102212\n800,00\nRSD"]'},
    'choose_acc_example': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Current account 5\n00210102213\n1.200,00\nRSD"]'},
    'exit_choose_acc': {'action': 'wait_and_click', 'locator': '//android.widget.FrameLayout[@resource-id=\'android:id/content\']/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]'},
    'current_acc_choose': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Saving account 1\nMB122333\n700\nRSD"]'},
    'saving_acc_choose_menu': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Saving account 1\nMB122333\n700,00\nRSD"]'},
    'current_acc_choose_menu': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Current account 3\n00210102211\n2.060,00\nRSD"]'},
    'credit_card_choose_menu': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Credit card account 1\n007\n0.00\nEUR"]'},
    'choose_acc_to_menu': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Choose account"]'},
    'data_choose_menu': {'action': 'wait_and_click', 'locator': '//android.view.View[@text="Monthly"]'},
    'monthly_choose_menu': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Monthly"]'},
    'quarterly_choose_menu': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Quarterly"]'},
    'yearly_choose_menu': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Yearly"]'},
    'exit_choose_menu': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Scrim"]'},
    'standing_order_choose_menu': {'action': 'wait_and_click', 'locator': '//android.widget.ScrollView/android.widget.EditText[2]'},
    'continue_choose_menu': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Continue"]'},
    'confirm_choose_menu': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Confirm"]'},
    'done_button_choose_menu': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Done"]'},
    'standing_order_chose': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Standing order"]'},
    'acc_from_standing_order': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Current account 4\n00210102212\n800,00\nRSD"]'},
    'acc_from_standing_order_chose': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Current account 5\n00210102213\n1.200,00\nRSD"]'},
    'exit_from_acc_standing': {'action': 'wait_and_click', 'locator': '//android.widget.FrameLayout[@resource-id=\'android:id/content\']/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]'},
    'standing_order_from_acc_chose': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="ten s kartou\n00210102101\n200,00\nRSD"]'},
    'acc_from_standing_order_choose': {'action': 'wait_and_click', 'locator': '//android.view.View[@content-desc="Saving account 1\nMB122333\n700,00\nRSD"]'},
    'amount_field_standing_order': {'action': 'wait_and_click', 'locator': '//android.widget.EditText'},
    'standing_order_nickname_filed': {'action': 'wait_and_click', 'locator': '//android.widget.ScrollView/android.widget.EditText[2]'},
    'show_more': {'action': 'wait_and_click', 'locator': '//android.widget.Button[@content-desc="Show more"]'},
    # Add other locators as needed
}



