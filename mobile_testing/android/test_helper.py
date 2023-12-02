import os
import socket
import time
from time import sleep
from typing import TYPE_CHECKING, Any, Callable
import json
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver
    from appium.webdriver.webelement import WebElement


def enter_text_and_hide_keyboard(driver, locator, text):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
    element.click()
    element.send_keys(text)
    driver.hide_keyboard()


# Appium server url
@pytest.fixture
def appium_server_url():
    return 'http://localhost:4723/wd/hub'


def wait_and_click(driver, locator):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
    element.click()


@pytest.fixture
def load_locators():
    with open('/Users/andrey/Desktop/appium_setup/mobile_testing/android/card_and_stikcers_data.json') as f:
        return json.load(f)


@pytest.fixture
def driver(appium_capabilities, appium_server_url):
    driver = webdriver.Remote(appium_server_url, options=appium_capabilities)
    yield driver
    if driver:
        driver.quit()


def swipe(driver):
    # Define swipe coordinates (adjust as needed)
    start_x = 300
    start_y = 500
    end_x = 100
    end_y = 100
    duration = 1000  # Duration in milliseconds

    # Perform the swipe action
    driver.swipe(start_x, start_y, end_x, end_y, duration)



class NoAvailablePortError(Exception):
    pass


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