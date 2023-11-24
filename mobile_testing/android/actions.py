# actions.py
from appium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def wait_and_click(driver, locator):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))
    element.click()


def enter_text_and_hide_keyboard(driver, locator, text):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))
    element.click()
    element.send_keys(text)
    driver.hide_keyboard()


def swipe(driver):
    # Define swipe coordinates (adjust as needed)
    start_x = 300
    start_y = 500
    end_x = 100
    end_y = 100
    duration = 1000  # Duration in milliseconds

    # Perform the swipe action
    driver.swipe(start_x, start_y, end_x, end_y, duration)
