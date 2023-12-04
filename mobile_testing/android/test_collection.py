import json
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from Card_and_Stikers import test_cards
from login import  test_login
from test_helper import( wait_and_click, appium_server_url, wait_for_element,
                         swipe, driver, enter_text_and_hide_keyboard, perform_actions_with_wait, appium_capabilities,
                         load_locators_card, load_locators)


@pytest.mark.run(order=1)
def test_scenario_1(test_login):
    assert True


@pytest.mark.run(order=2)
def test_scenario_2(test_login, test_cards):
    assert True
