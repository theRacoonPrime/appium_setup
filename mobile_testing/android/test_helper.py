import os
import socket
import time
from time import sleep
from typing import TYPE_CHECKING, Any, Callable
import json
import pytest
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver
    from appium.webdriver.webelement import WebElement


def wait_fun(driver, locator):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))
    element.click()


def enter_text_and_hide_keyboard(driver, locator, text):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
    element.click()
    element.send_keys(text)
    driver.hide_keyboard()


# Fixture for perform_actions_with_wait
@pytest.fixture
def perform_actions_with_wait(driver):
    def perform_actions(actions):
        for action in actions:
            action_type = action.get('action')
            locator = action.get('locator')
            text = action.get('text')

            if action_type == 'wait_and_click':
                wait_and_click(driver, locator)
            elif action_type == 'enter_text_and_hide_keyboard':
                enter_text_and_hide_keyboard(driver, locator, text)
            elif action_type == 'swipe':
                swipe(driver)

            # Add sleep or wait conditions as needed between actions
            sleep(1)

    return perform_actions


# Appium server url
@pytest.fixture
def appium_server_url():
    return 'http://localhost:4723/wd/hub'


def wait_and_click(driver, locator):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
    element.click()


@pytest.fixture
def load_locators_card():
    with open('/Users/andrey/Desktop/appium_setup/mobile_testing/android/card_and_stikcers_data.json') as f:
        return json.load(f)


# Load locators from JSON file
@pytest.fixture
def load_locators():
    with open('/Users/andrey/Desktop/appium_setup/mobile_testing/android/test_data.json') as f:
        return json.load(f)


@pytest.fixture
def appium_capabilities():
    # Load appium_capabilities from JSON file
    with open('/Users/andrey/Desktop/appium_setup/mobile_testing/android/capabilities.json') as f:
        capabilities = json.load(f)

    # Configure appium_capabilities using UiAutomator2Options
    capabilities = UiAutomator2Options().load_capabilities(capabilities)

    return capabilities


@pytest.fixture
def driver(appium_capabilities, appium_server_url):
    driver = webdriver.Remote(appium_server_url, options=appium_capabilities)
    yield driver
    if driver:
        driver.quit()


# Swipe action
def swipe(driver):
    # Define swipe coordinates (adjust as needed)
    start_x = 250
    start_y = 400
    end_x = 50
    end_y = 80
    duration = 1000  # Duration in milliseconds

    # Perform the swipe action
    driver.swipe(start_x, start_y, end_x, end_y, duration)


def get_available_from_port_range(from_port: int, to_port: int) -> int:
    """Returns available local port number.

    Args:
        from_port: The start port to search
        to_port: The end port to search

    Returns:
        int: available local port number which are found first

    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for port in range(from_port, to_port):
        try:
            if sock.connect_ex(('localhost', port)) != 0:
                return port
        finally:
            sock.close()

    raise NoAvailablePortError(f'No available port between {from_port} and {to_port}')


def is_ci() -> bool:
    """Returns if current execution is running on CI

    Returns:
        `True` if current executions is on CI
    """
    return os.getenv('CI', 'false') == 'true'


def wait_for_condition(method: Callable, timeout_sec: float = 5, interval_sec: float = 1) -> Any:
    """Wait while `method` returns the built-in objects considered false

    https://docs.python.org/3/library/stdtypes.html#truth-value-testing

    Args:
        method: The target method to be waited
        timeout: The timeout to be waited (sec.)
        interval_sec: The interval for wait (sec.)

    Returns:
        Any: value which `method` returns

    Raises:
        ValueError: When interval isn't more than 0

    """
    if interval_sec < 0:
        raise ValueError('interval_sec needs to be not less than 0')

    started = time.time()
    while time.time() - started <= timeout_sec:
        result = method()
        if result:
            break
        sleep(interval_sec)
    return result


def wait_for_element(driver: 'WebDriver', locator: str, value: str, timeout_sec: float = 10) -> 'WebElement':
    """Wait until the element located

    Args:
        driver: WebDriver instance
        locator: Locator like WebDriver, Mobile JSON Wire Protocol
            (e.g. `appium.webdriver.common.appiumby.AppiumBy.ACCESSIBILITY_ID`)
        value: Query value to locator
        timeout_sec: Maximum time to wait the element. If time is over, `TimeoutException` is thrown

    Raises:
        `selenium.common.exceptions.TimeoutException`

    Returns:
        The found WebElement
    """
    return WebDriverWait(driver, timeout_sec).until(EC.presence_of_element_located((locator, value)))