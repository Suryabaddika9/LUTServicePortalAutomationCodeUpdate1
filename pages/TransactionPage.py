from selenium.webdriver.common.by import By

from utilities.wait_helpers import wait_for_element


class TransactionPage:

    def __init__(self,driver):
        self.driver = driver

    transaction_success_msg_xpath = "//h4[@class='transactionCompletedText']"
    start_another_sale_button_xpath = "//button[normalize-space()='Start Another Sale']"
    close_button_xpath = "//button[normalize-space()='Close']"

    def click_on_close_button(self):
        close_butt = wait_for_element(self.driver,By.XPATH,self.close_button_xpath,timeout=20.0,condition="clickable")
        close_butt.click()

    def click_start_another_sale_button(self):
        start_another_sale_button = wait_for_element(self.driver, By.XPATH, self.start_another_sale_button_xpath,timeout=10,condition="clickable")
        start_another_sale_button.click()

    def verify_transaction_success_msg_is_displayed(self):
        success_msg = wait_for_element(self.driver, By.XPATH, self.transaction_success_msg_xpath,timeout=20,condition="visible")
        return success_msg.is_displayed()