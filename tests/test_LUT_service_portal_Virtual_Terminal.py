import allure
import pytest
import time
from utilities.wait_helpers import wait_for_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.HomePage import HomePage
from pages.TransactionPage import TransactionPage
from pages.VirtualTerminalPage import VirtualTerminalPage

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("setup_and_teardown_login","log_on_failure")
class TestLUTServicePortalVirtualTerminal:
    driver = None

    def navigate_to_virtual_terminal(self):
        homepage = HomePage(self.driver)
        homepage.waiting_for_js_loader_to_disappear()
        homepage.click_on_merchant_account_logo()
        homepage.click_on_virtual_terminal_option()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        main_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break

    def test_navigating_virtual_terminal(self):
        self.navigate_to_virtual_terminal()
        assert "Lüt Service Portal" in self.driver.title

    def test_payment_in_virtual_terminal_feature(self):

        self.navigate_to_virtual_terminal()
        main_window = self.driver.current_window_handle
        virtual_terminal_page = VirtualTerminalPage(self.driver)
        virtual_terminal_page.verify_virtual_terminal_header_is_displayed()
        virtual_terminal_page.enter_amount_into_sale_amount("123")
        #virtual_terminal_page.enter_amount_into_custom_tip_field("1")
        virtual_terminal_page.enter_pin_into_virtual_pin_input_field("5175961962")
        # Open OTP generator in a new tab
        self.driver.execute_script("window.open('https://totp.danhersam.com/', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait_for_element(self.driver, By.CSS_SELECTOR, "h1.title", timeout=10, condition="visible")
        secret_key = self.driver.find_element(By.XPATH,"//input[@placeholder='The secret key (in base-32 format)']")
        secret_key.clear()
        secret_key.send_keys("GUYTONJZGYYTSNRS")
        time_out = self.driver.find_element(By.XPATH, "//input[@placeholder='Usually 30']")

        time.sleep(2)
        time_out.send_keys("60")
        time.sleep(2)  # Wait for OTP to generate
        otp = self.driver.find_element(By.ID, "token").text
        # Switch back to Virtual Terminal tab
        self.driver.back()
        self.driver.switch_to.window(main_window)
        # Re-initialize page object if needed
        virtual_terminal_page = VirtualTerminalPage(self.driver)
        virtual_terminal_page.enter_pin_into_virtual_pin_input_field(otp)
        # Wait and click submit
        time.sleep(2)
        virtual_terminal_page.scroll_and_click_VT_submit_button()
        transaction_page = TransactionPage(self.driver)
        assert transaction_page.verify_transaction_success_msg_is_displayed()

    def test_virtual_terminal_start_another_sale_feature(self):
        self.navigate_to_virtual_terminal()
        main_window = self.driver.current_window_handle
        virtual_terminal_page = VirtualTerminalPage(self.driver)
        virtual_terminal_page.verify_virtual_terminal_header_is_displayed()
        virtual_terminal_page.enter_amount_into_sale_amount("123")
        virtual_terminal_page.enter_pin_into_virtual_pin_input_field("5175961962")
        # Open OTP generator in a new tab
        self.driver.execute_script("window.open('https://totp.danhersam.com/', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait_for_element(self.driver, By.CSS_SELECTOR, "h1.title", timeout=10, condition="visible")
        secret_key = self.driver.find_element(By.CSS_SELECTOR,
                                              "input[placeholder='The secret key (in base-32 format)']")
        secret_key.clear()
        secret_key.send_keys("GUYTONJZGYYTSNRS")
        time_out = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Usually 30']")
        time_out.clear()
        time_out.send_keys("60")
        time.sleep(2)  # Wait for OTP to generate
        otp = self.driver.find_element(By.ID, "token").text
        # Switch back to Virtual Terminal tab
        self.driver.close()
        self.driver.switch_to.window(main_window)
        # Re-initialize page object if needed
        virtual_terminal_page = VirtualTerminalPage(self.driver)
        virtual_terminal_page.enter_pin_into_virtual_pin_input_field(otp)
        # Wait and click submit
        virtual_terminal_page.scroll_and_click_VT_submit_button()
        transaction_page = TransactionPage(self.driver)
        transaction_page.click_start_another_sale_button()
        assert virtual_terminal_page.verify_virtual_pin_tag_box_is_displayed() or virtual_terminal_page.verify_virtual_terminal_header_is_displayed()

    def test_virtual_terminal_close_transaction_feature(self):
        home_window = self.driver.current_window_handle
        self.navigate_to_virtual_terminal()
        main_window = self.driver.current_window_handle
        virtual_terminal_page = VirtualTerminalPage(self.driver)
        virtual_terminal_page.verify_virtual_terminal_header_is_displayed()
        virtual_terminal_page.enter_amount_into_sale_amount("123")
        virtual_terminal_page.enter_pin_into_virtual_pin_input_field("5175961962")
        # Open OTP generator in a new tab
        self.driver.execute_script("window.open('https://totp.danhersam.com/', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait_for_element(self.driver, By.CSS_SELECTOR, "h1.title", timeout=10, condition="visible")
        secret_key = self.driver.find_element(By.CSS_SELECTOR,
                                              "input[placeholder='The secret key (in base-32 format)']")
        secret_key.clear()
        secret_key.send_keys("GUYTONJZGYYTSNRS")
        time_out = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Usually 30']")
        time_out.clear()
        time_out.send_keys("60")
        time.sleep(2)  # Wait for OTP to generate
        otp = self.driver.find_element(By.ID, "token").text
        # Switch back to Virtual Terminal tab
        self.driver.close()
        self.driver.switch_to.window(main_window)
        # Re-initialize page object if needed
        virtual_terminal_page = VirtualTerminalPage(self.driver)
        virtual_terminal_page.enter_pin_into_virtual_pin_input_field(otp)
        # Wait and click submit
        virtual_terminal_page.scroll_and_click_VT_submit_button()
        transaction_page = TransactionPage(self.driver)
        transaction_page.click_on_close_button()
        time.sleep(4)

        self.driver.switch_to.window(home_window)
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        assert home_page.verify_merchant_id_is_displayed()



