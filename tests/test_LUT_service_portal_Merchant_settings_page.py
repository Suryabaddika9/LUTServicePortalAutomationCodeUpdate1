import allure
import pytest
import time

from pages.AccountSettingsPage import AccountSettingsPage
from pages.MerchantSettingsPage import MerchantSettingsPage
from utilities.wait_helpers import wait_for_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.HomePage import HomePage
from pages.TransactionPage import TransactionPage
from pages.VirtualTerminalPage import VirtualTerminalPage

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("setup_and_teardown_login","log_on_failure")
class TestLUTServicePortalMerchantSettingsPage:
    driver = None

    def navigate_to_merchant_settings_page(self):
        homepage = HomePage(self.driver)
        homepage.waiting_for_js_loader_to_disappear()
        homepage.click_on_merchant_account_logo()
        homepage.click_on_merchant_settings_option()
        homepage.waiting_for_js_loader_to_disappear()


    def test_successfully_navigated_to_merchant_settings_page(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        assert mer_settings_page.verify_merchant_settings_text_is_displayed()

    def test_use_close_button_to_navigate_back_to_home_page(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        mer_settings_page.click_on_close_option()
        homepage.waiting_for_js_loader_to_disappear()
        assert homepage.verify_settlement_summary_widget_is_displayed()



