import pytest
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from test_helper import wait_for_element
from selenium.webdriver.support.ui import WebDriverWait
from test_helper import APIDEMO_PKG_NAME, BaseTestCase, is_ci
from appium.options.android import UiAutomator2Options
import json
from selenium.webdriver.support import expected_conditions as EC


# Load locators from JSON file
@pytest.fixture
def load_locators():
    with open('/Users/andrey/Desktop/appium_setup/mobile_testing/android/card_and_stikcers_data.json') as f:
        return json.load(f)


# Desired capabilities to specify the Android device and app details
@pytest.fixture
def appium_capabilities():
    # Load appium_capabilities from JSON file
    with open('/Users/andrey/Desktop/appium_setup/mobile_testing/android/capabilities.json') as f:
        capabilities = json.load(f)

    # Configure appium_capabilities using UiAutomator2Options
    capabilities = UiAutomator2Options().load_capabilities(capabilities)

    return capabilities


# Appium server url
@pytest.fixture
def appium_server_url():
    return 'http://localhost:4723/wd/hub'


@pytest.fixture
def driver(appium_capabilities, appium_server_url):
    driver = webdriver.Remote(appium_server_url, options=appium_capabilities)
    yield driver
    if driver:
        driver.quit()


# Common actions
def wait_and_click(driver, locator):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
    element.click()


def enter_text_and_hide_keyboard(driver, locator, text):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((AppiumBy.XPATH, locator)))
    element.click()
    element.send_keys(text)
    driver.hide_keyboard()


# Swipe action
def swipe(driver):
    # Define swipe coordinates (adjust as needed)
    start_x = 300
    start_y = 500
    end_x = 100
    end_y = 100
    duration = 1000  # Duration in milliseconds

    # Perform the swipe action
    driver.swipe(start_x, start_y, end_x, end_y, duration)


def test_tap(self) -> None:
    el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')
    action = TouchAction(self.driver)
    action.tap(el).perform()
    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Bouncing Balls')
    assert el is not None


def test_tap_x_y(self) -> None:
    el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')
    action = TouchAction(self.driver)
    action.tap(el, 100, 10).perform()

    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Bouncing Balls')
    assert el is not None


@pytest.mark.skipif(condition=is_ci(), reason='Need to fix flaky test during running on CI.')
def test_tap_twice(self) -> None:
    el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Text')
    action = TouchAction(self.driver)
    action.tap(el).perform()

    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'LogTextBox')
    action.tap(el).perform()

    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Add')
    action.tap(el, count=2).perform()

    els = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.TextView')
    assert 'This is a test\nThis is a test\n' == els[1].get_attribute('text')


def test_press_and_immediately_release(self) -> None:
    el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')
    action = TouchAction(self.driver)
    action.press(el).release().perform()

    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Bouncing Balls')
    assert el is not None


def test_press_and_immediately_release_x_y(self) -> None:
    el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')
    action = TouchAction(self.driver)
    action.press(el, 100, 10).release().perform()

    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Bouncing Balls')
    assert el is not None


def test_press_and_wait(self) -> None:
    self._move_to_custom_adapter()
    action = TouchAction(self.driver)

    el = wait_for_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("People Names")')
    action.press(el).wait(2000).perform()

    # 'Sample menu' only comes up with a long press, not a press
    el = wait_for_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sample menu")')
    assert el is not None


def test_press_and_moveto(self) -> None:
    el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Content')
    el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')

    action = TouchAction(self.driver)
    action.press(el1).move_to(el2).release().perform()

    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Views')
    assert el is not None


def test_press_and_moveto_x_y(self) -> None:
    el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Content')
    el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='App')

    action = TouchAction(self.driver)
    action.press(el1).move_to(el2, 100, 100).release().perform()

    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Views')
    assert el is not None


def test_long_press(self) -> None:
    self._move_to_custom_adapter()
    action = TouchAction(self.driver)

    el = wait_for_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("People Names")')
    action.long_press(el).perform()

    # 'Sample menu' only comes up with a long press, not a tap
    el = wait_for_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sample menu")')
    assert el is not None


@pytest.mark.skipif(condition=is_ci(), reason='Skip since this check is low robust due to hard-coded position.')
def test_long_press_x_y(self) -> None:
    self._move_to_custom_adapter()
    action = TouchAction(self.driver)

    # the element "People Names" is located at 430:310 (top left corner)
    # location can be changed by phone resolusion, OS version
    action.long_press(x=430, y=310).perform()

    # 'Sample menu' only comes up with a long press, not a tap
    el = wait_for_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sample menu")')
    assert el is not None


def test_drag_and_drop(self) -> None:
    self._move_to_views()
    action = TouchAction(self.driver)

    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Drag and Drop')
    action.tap(el).perform()

    dd3 = wait_for_element(self.driver, AppiumBy.ID, '{}:id/drag_dot_3'.format(APIDEMO_PKG_NAME))
    dd2 = self.driver.find_element(by=AppiumBy.ID, value='{}:id/drag_dot_2'.format(APIDEMO_PKG_NAME))

    # dnd is stimulated by longpress-move_to-release
    action.long_press(dd3).move_to(dd2).release().perform()

    el = wait_for_element(self.driver, AppiumBy.ID, '{}:id/drag_result_text'.format(APIDEMO_PKG_NAME))
    assert 'Dropped!' in el.text


def test_driver_drag_and_drop(self) -> None:
    self._move_to_views()
    action = TouchAction(self.driver)

    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Drag and Drop')
    action.tap(el).perform()

    dd3 = wait_for_element(self.driver, AppiumBy.ID, '{}:id/drag_dot_3'.format(APIDEMO_PKG_NAME))
    dd2 = self.driver.find_element(by=AppiumBy.ID, value='{}:id/drag_dot_2'.format(APIDEMO_PKG_NAME))

    self.driver.drag_and_drop(dd3, dd2)

    el = wait_for_element(self.driver, AppiumBy.ID, '{}:id/drag_result_text'.format(APIDEMO_PKG_NAME))
    assert 'Dropped!' in el.text


def test_driver_swipe(self) -> None:
    el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views')
    action = TouchAction(self.driver)
    action.tap(el).perform()

    with pytest.raises(NoSuchElementException):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='ImageView')

    self.driver.swipe(100, 1000, 100, 100, 800)
    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'ImageView')
    assert el is not None


def _move_to_views(self) -> None:
    el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Content')
    el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')
    self.driver.scroll(el1, el2)

    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Views')
    action = TouchAction(self.driver)
    action.tap(el).perform()


def _move_to_custom_adapter(self) -> None:
    self._move_to_views()
    action = TouchAction(self.driver)

    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Expandable Lists')
    action.tap(el).perform()

    el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, '1. Custom Adapter')
    action.tap(el).perform()