import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
# from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput


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
def click_element(driver, locator):
    element = driver.find_element(by=AppiumBy.XPATH, value=locator)
    element.click()


def enter_text(driver, locator, text):
    element = driver.find_element(by=AppiumBy.XPATH, value=locator)
    element.click()
    element.send_keys(text)


# Test data

locators = {
    'already_have_account': '//android.widget.Button[@content-desc="I already have account"]',
    'continue_button': '//android.widget.Button[@content-desc="Continue"]',
    'password_field_1': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout'
                        '/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android'
                        '.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]',
    'password_field_2': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout'
                        '/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android'
                        '.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]',
    'accept_button': '//android.widget.Button[@content-desc="Accept"]',
    'thanks_button': '//android.widget.Button[@content-desc="Thanks, but not now"]',
    'go_to_app_button': '//android.widget.Button[@content-desc="Go to the app"]',
    'password_field_general': '//android.widget.EditText',
    'acc_button': '//android.widget.ScrollView/android.view.View[2]/android.view.View/android.view.View[1]',
    'tree_dot': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android'
                '.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View['
                '1]/android.widget.Button[2]',
    'copy_button': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout'
                   '/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view'
                   '.View[2]/android.view.View/android.view.View[2]',
    'card_button': '//android.widget.Button[@content-desc="Cards"]',
    'exit_card_button': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout'
                        '/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android'
                        '.view.View[1]/android.widget.Button[1]',
    'payment_limits_button': '//android.widget.Button[@content-desc="Payment Limits"]',
    'statement_button': '//android.widget.Button[@content-desc="Statements"]',
    'balance_information_button': '//android.view.View[@content-desc="Balance information"]',
    'account_info_button': '//android.view.View[@content-desc="Account information"]',
    'standing_order_button': '//android.view.View[@content-desc="Standing order"]',
    'exit_payment_limit': '//android.widget.Button',
    'statement_exit_button': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget'
                             '.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android'
                             '.view.View/android.view.View[1]/android.widget.Button[1]',
    'acc_info_button': '//android.view.View[@content-desc="Balance information"]',
    'exit_accinfo_button': '//android.view.View[@content-desc="Scrim"]',
    'exit_balance_info': '//android.view.View[@content-desc="Scrim"]',
    'standing_order': '//android.view.View[@content-desc="Standing order"]',
    'device_name': '//android.widget.Button[@content-desc="Continue"]',
    'exit_button': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout'
                   '/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view'
                   '.View[1]/android.widget.Button',
    'current_acc_rsd': '//android.view.View[@content-desc="Current account 1200RSD00210102101"]',
    'current_acc_usd': '// android.view.View[ @ content - desc = "Current account 2200.00USD00210102202"]',
    'current_acc_eu': '//android.view.View[@content-desc="Authorized account 3 700.00 EUR 0898528798"]',
    'new_payment': '//android.widget.Button[@content-desc="New payment"]',
    'amount_field': '//android.widget.EditText',
    'choose_acc': '//android.widget.Button[@content-desc="Choose account"]',
}


def test_account(driver):
    driver.implicitly_wait(20)

    click_element(driver, locators['already_have_account'])
    click_element(driver, locators['continue_button'])
    click_element(driver, locators['continue_button'])

    wait = WebDriverWait(driver, 20)

    enter_text(driver, locators['password_field_1'], '123456')
    # Hide the keyboard after entering text in the first password field
    driver.hide_keyboard()

    enter_text(driver, locators['password_field_2'], '123456')
    # Hide the keyboard after entering text in the second password field
    driver.hide_keyboard()

    click_element(driver, locators['continue_button'])
    click_element(driver, locators['thanks_button'])
    click_element(driver, locators['device_name'])
    click_element(driver, locators['go_to_app_button'])

    wait = WebDriverWait(driver, 20)

    enter_text(driver, locators['password_field_general'], '123456')
    click_element(driver, locators['accept_button'])
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, locators['acc_button'])))
    click_element(driver, locators['acc_button'])
    sleep(1)
    click_element(driver, locators['new_payment'])
    sleep(1)
    click_element(driver, locators['choose_acc'])
    sleep(1)
    click_element(driver, locators['exit_button'])
    enter_text(driver, locators['amount_field'], '123456')
    sleep(1)
    click_element(driver, locators['exit_button'])
    sleep(1)
    click_element(driver, locators['tree_dot'])
    sleep(1)
    click_element(driver, locators['copy_button'])
    sleep(1)
    click_element(driver, locators['card_button'])
    click_element(driver, locators['exit_card_button'])
    sleep(1)
    click_element(driver, locators['payment_limits_button'])
    sleep(1)
    click_element(driver, locators['exit_payment_limit'])
    click_element(driver, locators['statement_button'])
    sleep(1)
    click_element(driver, locators['statement_exit_button'])
    sleep(1)
    click_element(driver, locators['balance_information_button'])
    sleep(1)
    click_element(driver, locators['exit_balance_info'])
    sleep(2)
    click_element(driver, locators['account_info_button'])
    sleep(1)
    click_element(driver, locators['exit_accinfo_button'])
    sleep(1)
    click_element(driver, locators['standing_order'])
    click_element(driver, locators['exit_button'])
    sleep(1)

    # //android.view.View[@content-desc="Current account 1200RSD00210102101"]
    # // android.view.View[ @ content - desc = "Current account 2200.00USD00210102202"]
    #  //android.view.View[@content-desc="Authorized account 3 700.00 EUR 0898528798"]
