import allure
import pytest
import time

from pages.AccountSettingsPage import AccountSettingsPage
from pages.ChargeBacksPage import ChargeBacksPage
from pages.MerchantSettingsPage import MerchantSettingsPage
from pages.MyReportsPage import MyReportsPage
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

    def navigate_to_my_reports_option(self):
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        home_page.click_on_my_reports_option()
        home_page.waiting_for_js_loader_to_disappear()

    def test_verify_report_category_report_type_options_are_displayed(self):
        self.navigate_to_my_reports_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        my_reports_page = MyReportsPage(self.driver)
        assert my_reports_page.verify_report_category_and_report_type_options_are_displayed()

    def test_verify_no_data_logo_and_text_are_displayed(self):
        self.navigate_to_my_reports_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        my_reports_page = MyReportsPage(self.driver)
        assert my_reports_page.verify_no_data_logo_and_text_are_displayed()

    def test_verify_summary_reports_in_report_category(self):
        self.navigate_to_my_reports_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        my_reports_page = MyReportsPage(self.driver)
        my_reports_page.select_summary_reports_option_from_report_category()
        time.sleep(3)

