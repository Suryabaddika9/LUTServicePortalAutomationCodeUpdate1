import allure
import pytest
import time

from pages.AccountSettingsPage import AccountSettingsPage
from utilities.wait_helpers import wait_for_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.HomePage import HomePage
from pages.TransactionPage import TransactionPage
from pages.VirtualTerminalPage import VirtualTerminalPage

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("setup_and_teardown_login","log_on_failure")
class TestLUTServicePortalAccountSettingsPage:
    driver = None

    def navigate_to_account_settings_page(self):
        homepage = HomePage(self.driver)
        homepage.waiting_for_js_loader_to_disappear()
        homepage.click_on_merchant_account_logo()
        homepage.click_on_account_settings_option()

    def test_successfully_navigate_to_account_settings_page(self):
        homepage = HomePage(self.driver)
        self.navigate_to_account_settings_page()
        homepage.waiting_for_js_loader_to_disappear()
        acc_success_page = AccountSettingsPage(self.driver)
        assert acc_success_page.verify_profile_and_settings_text_is_displayed()

    def test_use_close_button_to_navigate_back_to_home_page(self):
        homepage = HomePage(self.driver)
        self.navigate_to_account_settings_page()
        homepage.waiting_for_js_loader_to_disappear()
        acc_success_page = AccountSettingsPage(self.driver)
        assert acc_success_page.verify_profile_and_settings_text_is_displayed()
        acc_success_page.click_on_close_option()
        homepage.waiting_for_js_loader_to_disappear()
        assert homepage.verify_settlement_summary_widget_is_displayed()

    def test_click_on_update_info_link(self):
        homepage = HomePage(self.driver)
        self.navigate_to_account_settings_page()
        homepage.waiting_for_js_loader_to_disappear()
        acc_success_page = AccountSettingsPage(self.driver)
        acc_success_page.click_on_update_info_link()
        homepage.waiting_for_js_loader_to_disappear()
        assert acc_success_page.verify_personal_info_popup_is_displayed()

    def test_click_on_update_info_link_and_using_close_option_to_go_back_to_acc_settings_page(self):
        homepage = HomePage(self.driver)
        self.navigate_to_account_settings_page()
        homepage.waiting_for_js_loader_to_disappear()
        acc_success_page = AccountSettingsPage(self.driver)
        acc_success_page.click_on_update_info_link()
        homepage.waiting_for_js_loader_to_disappear()
        assert acc_success_page.verify_personal_info_popup_is_displayed()
        acc_success_page = AccountSettingsPage(self.driver)
        acc_success_page.click_on_popup_close_option()
        assert acc_success_page.verify_profile_and_settings_text_is_displayed()

    def test_click_on_change_email_link(self):
        homepage = HomePage(self.driver)
        self.navigate_to_account_settings_page()
        homepage.waiting_for_js_loader_to_disappear()
        acc_success_page = AccountSettingsPage(self.driver)
        acc_success_page.click_on_change_email_link()
        homepage.waiting_for_js_loader_to_disappear()
        assert acc_success_page.verify_change_my_mail_popup_is_displayed()

    def test_click_on_change_email_link_and_using_close_option_to_go_back_to_acc_settings_page(self):
        homepage = HomePage(self.driver)
        self.navigate_to_account_settings_page()
        homepage.waiting_for_js_loader_to_disappear()
        acc_success_page = AccountSettingsPage(self.driver)
        acc_success_page.click_on_change_email_link()
        homepage.waiting_for_js_loader_to_disappear()
        assert acc_success_page.verify_change_my_mail_popup_is_displayed()
        acc_success_page = AccountSettingsPage(self.driver)
        acc_success_page.click_on_popup_close_option()
        assert acc_success_page.verify_profile_and_settings_text_is_displayed()

    def test_click_on_change_password_link(self):
        homepage = HomePage(self.driver)
        self.navigate_to_account_settings_page()
        homepage.waiting_for_js_loader_to_disappear()
        acc_success_page = AccountSettingsPage(self.driver)
        acc_success_page.click_on_change_password_link()
        homepage.waiting_for_js_loader_to_disappear()
        assert acc_success_page.verify_change_my_password_popup_is_displayed()

    def test_click_on_change_password_link_and_click_on_update_password_in_popup_without_entering_values_in_fields(self):
        homepage = HomePage(self.driver)
        self.navigate_to_account_settings_page()
        homepage.waiting_for_js_loader_to_disappear()
        acc_success_page = AccountSettingsPage(self.driver)
        acc_success_page.click_on_change_password_link()
        homepage.waiting_for_js_loader_to_disappear()
        acc_success_page.click_on_change_password_button_in_popup()
        homepage.waiting_for_js_loader_to_disappear()
        assert acc_success_page.verify_error_field_text_in_popup_is_displayed()

    def test_click_on_change_password_link_and_using_close_option_to_go_back_to_acc_settings_page(self):
        homepage = HomePage(self.driver)
        self.navigate_to_account_settings_page()
        homepage.waiting_for_js_loader_to_disappear()
        acc_success_page = AccountSettingsPage(self.driver)
        acc_success_page.click_on_change_password_link()
        homepage.waiting_for_js_loader_to_disappear()
        assert acc_success_page.verify_change_my_password_popup_is_displayed()
        acc_success_page = AccountSettingsPage(self.driver)
        acc_success_page.click_on_popup_close_option()
        assert acc_success_page.verify_profile_and_settings_text_is_displayed()
