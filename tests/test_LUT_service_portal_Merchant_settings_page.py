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

    def test_click_on_update_info_link(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        mer_settings_page.click_on_update_info_link()
        assert mer_settings_page.verify_business_info_popup_is_displayed()

    def test_click_on_update_info_link_and_close_option_to_go_back_to_merchant_settings_page(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        mer_settings_page.click_on_update_info_link()
        mer_settings_page.click_on_close_popup_option()
        assert mer_settings_page.verify_merchant_settings_text_is_displayed()

    def test_financial_info_and_pricing_section(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        mer_settings_page.click_on_financial_info_and_pricing_option()
        homepage.waiting_for_js_loader_to_disappear()
        mer_settings_page.click_on_update_info_link()
        assert mer_settings_page.verify_financial_info_popup_is_displayed()

    def test_financial_info_and_pricing_section_and_closing_popup(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        mer_settings_page.click_on_financial_info_and_pricing_option()
        homepage.waiting_for_js_loader_to_disappear()
        mer_settings_page.click_on_update_info_link()
        mer_settings_page.verify_financial_info_popup_is_displayed()
        mer_settings_page.click_on_close_popup_option()
        assert mer_settings_page.verify_merchant_settings_text_is_displayed()

    def test_tips_and_processing_fee_section(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        homepage.waiting_for_js_loader_to_disappear()
        mer_settings_page.click_on_tips_and_processing_fee_option()
        assert mer_settings_page.verify_instore_tipping_and_processing_fee_options_are_displayed()

    def test_online_shopping_section(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        homepage.waiting_for_js_loader_to_disappear()
        mer_settings_page.click_on_online_shopping_option()
        assert mer_settings_page.verify_lut_buy_now_and_lut_orders_texts_are_displayed()

    def test_manage_users_option(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        mer_settings_page.click_on_manage_users_option()
        assert mer_settings_page.verify_name_is_displayed_in_manage_users()

    def test_add_user_option_in_manage_users(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        mer_settings_page.click_on_manage_users_option()
        mer_settings_page.verify_name_is_displayed_in_manage_users()
        mer_settings_page.click_on_add_user_button()
        assert mer_settings_page.verify_add_user_text_is_displayed_in_add_user_popup()

    def test_add_user_option_in_manage_users_and_closing(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        mer_settings_page.click_on_manage_users_option()
        mer_settings_page.verify_name_is_displayed_in_manage_users()
        mer_settings_page.click_on_add_user_button()
        mer_settings_page.verify_add_user_text_is_displayed_in_add_user_popup()
        mer_settings_page.click_on_close_popup_option()
        assert mer_settings_page.verify_name_is_displayed_in_manage_users()

    def test_verifying_error_msg_in_add_user_option_in_manage_users_by_clicking_add_user_button_without_entering_values(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        mer_settings_page.click_on_manage_users_option()
        mer_settings_page.verify_name_is_displayed_in_manage_users()
        mer_settings_page.click_on_add_user_button()
        mer_settings_page.click_on_add_user_button_in_popup()
        assert mer_settings_page.verify_warning_msg_about_all_fields_in_add_user_popup_is_displayed()
        mer_settings_page.click_on_close_popup_option()

    def test_verifying_error_msgs_in_email_and_number_fields_in_add_user_option_in_manage_users_by_clicking_add_user_button_without_entering_values(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        mer_settings_page.click_on_manage_users_option()
        mer_settings_page.verify_name_is_displayed_in_manage_users()
        mer_settings_page.click_on_add_user_button()
        mer_settings_page.click_on_email_field_in_add_user_popup()
        mer_settings_page.click_on_phone_num_field_in_add_user_popup()
        mer_settings_page.click_on_add_user_button_in_popup()
        assert mer_settings_page.verify_warning_msg_about_all_fields_in_add_user_popup_is_displayed() and mer_settings_page.verify_email_and_phone_num_warning_msg_are_displayed()
        mer_settings_page.click_on_close_popup_option()

    def test_manage_locations_option(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        mer_settings_page.click_on_manage_locations_option()
        assert mer_settings_page.verify_no_locations_available_text_is_displayed()

    def test_add_locations_button_in_manage_locations_option(self):
        homepage = HomePage(self.driver)
        self.navigate_to_merchant_settings_page()
        mer_settings_page = MerchantSettingsPage(self.driver)
        mer_settings_page.click_on_manage_locations_option()
        mer_settings_page.verify_no_locations_available_text_is_displayed()
        mer_settings_page.click_on_add_location_button_in_manage_locations_option()
        assert mer_settings_page.verify_add_location_popup_text_is_displayed()
        mer_settings_page.click_on_close_popup_option()





