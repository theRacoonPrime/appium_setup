import pytest
from test_helper import( wait_and_click, appium_server_url, wait_for_element,
                         swipe, driver, enter_text_and_hide_keyboard, perform_actions_with_wait, appium_capabilities,
                         load_locators_card, load_locators)
from Card_and_Stikers import test_cards
from login import test_login, negative_test_login
from account_test import payment
from current_account import current_account
from main_menu import test_main_menu
from activefilters_test import test_activities_filters
from card_detail_test import test_card_detail
from count_and_transactions_test import test_count_and_transaction
from Deposits_products import test_deposits_products
from incoming_transactions_test import test_incoming_transaction
from Loan_products import test_loan_products


@pytest.mark.run(order=1)
def test_scenario_1(test_login):
    assert True


@pytest.mark.run(order=2)
def test_scenario_2(negative_test_login):
    assert True


@pytest.mark.run(order=3)
def test_scenario_3(test_login, test_cards):
    assert True


@pytest.mark.run(order=4)
def test_scenario_4(test_login, test_card_detail):
    assert True


@pytest.mark.run(order=5)
def test_scenario_5(test_login, current_account):
    assert True


@pytest.mark.run(order=6)
def test_scenario_6(test_login, payment):
    assert True


@pytest.mark.run(order=7)
def test_scenario_7(test_login, test_count_and_transaction):
    assert True


@pytest.mark.run(order=8)
def test_scenario_8(test_login, test_deposits_products):
    assert True


@pytest.mark.run(order=9)
def test_scenario_9(test_login, test_incoming_transaction):
    assert True


@pytest.mark.run(order=10)
def test_scenario_10(test_login, test_loan_products):
    assert True


@pytest.mark.run(order=11)
def test_scenario_11(test_login, test_main_menu):
    assert True


@pytest.mark.run(order=13)
def test_scenario_12(test_login, test_payments_domestic):
    assert True


@pytest.mark.run(order=13)
def test_scenario_13(test_login, test_cards_negative):
    assert True


@pytest.mark.run(order=14)
def test_scenario_14(test_login, test_current_account_negative):
    assert True


@pytest.mark.run(order=15)
def test_scenario_15(test_login, test_current_account_negative):
    assert True


@pytest.mark.run(order=16)
def test_scenario_16(test_login, test_count_and_transaction_negative):
    assert True


@pytest.mark.run(order=17)
def test_scenario_17(test_login, test_deposits_products_negative):
    assert True


@pytest.mark.run(order=18)
def test_scenario_18(test_login, test_incoming_transaction_negative):
    assert True

