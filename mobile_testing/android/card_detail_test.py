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

# Read locators from JSON file
with open('/Users/andrey/Desktop/appium_setup/mobile_testing/android/test_data.json') as f:
    locators = json.load(f)


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