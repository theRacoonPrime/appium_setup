import pytest
from test_helper import( wait_and_click, appium_server_url, wait_for_element,
                         swipe, driver, enter_text_and_hide_keyboard, perform_actions_with_wait, appium_capabilities,
                         load_locators_card, load_locators)
from Card_and_Stikers import test_cards
from login import test_login
from account_test import payment
from current_account import current_account


@pytest.mark.run(order=1)
def test_scenario_1(test_login):
    assert True


@pytest.mark.run(order=2)
def test_scenario_2(test_login, test_cards):
    assert True


@pytest.mark.run(order=3)
def test_scenario_3(test_login, payment):
    assert True


@pytest.mark.run(order=4)
def test_scenario_4(test_login, current_account):
    assert True
