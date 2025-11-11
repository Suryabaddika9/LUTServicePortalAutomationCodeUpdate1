import time

import allure
import pytest
from selenium.webdriver.support.expected_conditions import alert_is_present
from pages.FAQPage import FAQPage
from pages.HomePage import HomePage
from pages.MyAccountsPage import MyAccountsPage
from pages.ServiceTicketsPage import ServiceTicketsPage

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("setup_and_teardown_login","log_on_failure")
class TestLUTServicePortalHomePageNavbarFunctionality:
    driver = None
    def test_home_page_login_verification(self):
        home_page = HomePage(self.driver)
        assert home_page.verify_merchant_id_is_displayed()

    def test_home_page_top_navbar_merchant_view_option_verification(self):
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        home_page.click_on_merchant_view_dropdown()
        my_accounts_page = MyAccountsPage(self.driver)
        my_accounts_page.verify_my_accounts_image_is_displayed()
        my_accounts_page.click_next_button()
        home_page.waiting_for_js_loader_to_disappear()
        home_page.verify_merchant_id_is_displayed()

    def test_home_page_top_navbar_search_invalid_transaction_ID_functionality(self):
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        home_page.enter_text_into_transaction_ID_field("1234567")
        assert home_page.verify_transaction_id_not_found_text_is_displayed()

    def test_home_page_top_navbar_search_valid_transaction_ID_functionality(self):
        pass

    def test_home_page_top_navbar_support_service_tickets_functionality(self):
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        home_page.click_on_support_option()
        home_page.click_on_service_tickets_option()
        home_page.waiting_for_js_loader_to_disappear()
        service_tickets_page = ServiceTicketsPage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        service_tickets_page.verify_service_tickets_text_is_displayed()
        service_tickets_page.click_on_service_tickets_card_container_cancel_option()
        service_tickets_page.click_on_close_button()
        home_page.waiting_for_js_loader_to_disappear()
        assert home_page.verify_settlement_summary_widget_is_displayed()

    def test_check_notification_icon_functionality(self):
        home_page = HomePage(self.driver)
        home_page.click_on_notification_icon()
        assert home_page.verify_notification_box_is_displayed()
        time.sleep(4)


    def test_check_FAQ_option_and_FAQ_close_option_functionality(self):
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        home_page.click_on_support_option()
        home_page.click_on_FAQ_option()
        home_page.waiting_for_js_loader_to_disappear()
        faq_option_page = FAQPage(self.driver)
        assert faq_option_page.verify_FAQ_sidebar_with_options_is_displayed()
        faq_option_page.click_on_close_option()
        home_page.waiting_for_js_loader_to_disappear()
        home_page.verify_settlement_summary_widget_is_displayed()
        time.sleep(4)

    def test_all_FAQs_are_displayed(self):
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        home_page.click_on_support_option()
        home_page.click_on_FAQ_option()
        home_page.waiting_for_js_loader_to_disappear()
        faq_option_page = FAQPage(self.driver)
        assert faq_option_page.left_number_of_FAQ_questions() == faq_option_page.right_number_of_FAQ_questions()
        time.sleep(4)

    def test_support_option_call_functionality(self):
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        home_page.click_on_support_option()
        home_page.click_on_contactus_section_phone_option()
        home_page.waiting_for_js_loader_to_disappear()
        assert alert_is_present()
        time.sleep(4)

    def test_support_option_email_functionality(self):
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        home_page.click_on_support_option()
        home_page.waiting_for_js_loader_to_disappear()
        home_page.click_on_contact_us_section_email_option()
        home_page.waiting_for_js_loader_to_disappear()
        time.sleep(4)











