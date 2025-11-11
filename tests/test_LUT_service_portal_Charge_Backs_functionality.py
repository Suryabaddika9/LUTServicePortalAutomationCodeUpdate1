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
class TestLUTServicePortalChargeBacksFunctionality:
    driver = None

    def navigate_to_charge_backs_option(self):
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        home_page.click_on_charge_backs_option()
        home_page.waiting_for_js_loader_to_disappear()


    def test_verify_successfully_navigated_to_charge_backs_functionality(self):
        home_page = HomePage(self.driver)
        self.navigate_to_charge_backs_option()
        home_page.waiting_for_js_loader_to_disappear()
        charge_backs_page = ChargeBacksPage(self.driver)
        assert charge_backs_page.verify_charge_backs_widget_heading_is_displayed()

    def test_verify_unresolved_and_new_charge_backs_kpis_are_displayed(self):
        home_page = HomePage(self.driver)
        self.navigate_to_charge_backs_option()
        home_page.waiting_for_js_loader_to_disappear()
        charge_backs_page = ChargeBacksPage(self.driver)
        assert charge_backs_page.verify_unresolved_charge_backs_kpi_is_displayed() and charge_backs_page.verify_new_charge_backs_kpi_is_displayed()


    def test_verify_filters_widget_is_displayed(self):
        home_page = HomePage(self.driver)
        self.navigate_to_charge_backs_option()
        home_page.waiting_for_js_loader_to_disappear()
        charge_backs_page = ChargeBacksPage(self.driver)
        assert charge_backs_page.verify_filters_widget_is_displayed()

    def test_verifying_display_status_of_filters_components(self):
        self.navigate_to_charge_backs_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        charge_backs_page = ChargeBacksPage(self.driver)
        assert charge_backs_page.verify_all_filter_options_are_available()

    def test_verifying_display_status_of_charge_backs_table_container(self):
        self.navigate_to_charge_backs_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        charge_backs_page = ChargeBacksPage(self.driver)
        assert charge_backs_page.verify_charge_backs_table_container_is_displayed()



