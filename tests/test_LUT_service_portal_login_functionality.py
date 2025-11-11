import allure
import faker
import pytest
from faker import Faker

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage

@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.usefixtures("setup_and_teardown")
class TestLUTServicePortalLoginFunctionality:
    driver = None


    fake = Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()

    def test_service_portal_login_with_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_application("bankdata2@gmail.com","Admin@123")
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        assert home_page.verify_merchant_id_is_displayed()

    def test_service_portal_login_with_invalid_credentials_invalid_format(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_application(self.name,self.password)
        assert login_page.verify_email_error_msg_is_displayed() or login_page.verify_password_error_msg_is_displayed()

    def test_service_portal_login_with_invalid_credentials_in_format(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_application(self.email,self.password)
        assert login_page.verify_invalid_user_alert_is_displayed()

    def test_service_portal_login_with_invalid_username_valid_password(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_application(self.email, "Admin@123")
        assert login_page.verify_invalid_user_alert_is_displayed()

    def test_service_portal_login_with_valid_username_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_application("bankdata2@gmail.com","123456789")
        assert login_page.verify_invalid_credentials_error_msg_is_displayed()

    def test_service_portal_login_without_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login_to_application("","")
        assert login_page.verify_email_error_msg_is_displayed()

