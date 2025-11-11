from selenium.webdriver.common.by import By

from utilities.wait_helpers import wait_for_element


class ServiceTicketsPage:

    def __init__(self,driver):
        self.driver = driver

    service_ticket_text_css_selector="h5[class='modal-title'] p"
    service_ticket_card_container_cancel_option_css_selector = "h5[class='modal-title'] div svg path"
    close_button_css_selector = "div[class='service-tkts-header-close-btn'] p"

    def verify_service_tickets_text_is_displayed(self):
        service_tickets_text = wait_for_element(self.driver, By.CSS_SELECTOR, self.service_ticket_text_css_selector,timeout=10,condition="visible")
        return service_tickets_text.is_displayed()

    def click_on_service_tickets_card_container_cancel_option(self):
        self.driver.find_element(By.CSS_SELECTOR,self.service_ticket_card_container_cancel_option_css_selector).click()

    def click_on_close_button(self):
        close_button = wait_for_element(self.driver, By.CSS_SELECTOR, self.close_button_css_selector, timeout=20, condition="clickable")
        close_button.click()