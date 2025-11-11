import allure
import pytest
import time

from pages.AccountSettingsPage import AccountSettingsPage
from pages.ChargeBacksPage import ChargeBacksPage
from pages.MerchantSettingsPage import MerchantSettingsPage
from utilities.wait_helpers import wait_for_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.HomePage import HomePage
from pages.TransactionPage import TransactionPage
from pages.VirtualTerminalPage import VirtualTerminalPage

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("setup_and_teardown_login","log_on_failure")
class TestLUTServicePortalMyReportsFunctionality:
    driver = None

    def test_navigate_to_my_reports_option(self):
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        home_page.click_on_my_reports_option()
        home_page.waiting_for_js_loader_to_disappear()
        time.sleep(3)