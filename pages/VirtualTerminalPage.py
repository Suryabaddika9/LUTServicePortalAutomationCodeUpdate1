from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from utilities.wait_helpers import wait_for_element
from utilities.scroll_and_click_button import scroll_and_click_button



class VirtualTerminalPage:

    def __init__(self,driver):
        self.driver = driver

    virtual_terminal_header_xpath = "//div[@class='virtual-terminal-Header-h4']"
    sale_amount_input_xpath = "//input[@placeholder='Enter Sale Amount']"
    virtual_pin_input_xpath = "//input[@placeholder='Enter 16 Digit PIN']"
    vt_submit_button_css_selector = "button[type='button']"
    virtual_pin_tag_box_xpath = "//div[@class='virtualPintag null']"


    def verify_virtual_pin_tag_box_is_displayed(self):
        vp_box = wait_for_element(self.driver,By.XPATH,self.virtual_pin_tag_box_xpath,timeout=20,condition="visible")
        return vp_box.is_displayed()

    def scroll_and_click_VT_submit_button(self):
        scroll_and_click_button(self.driver,By.CSS_SELECTOR,self.vt_submit_button_css_selector,timeout=20)

    def enter_pin_into_virtual_pin_input_field(self,text):
        vp_input_field = wait_for_element(self.driver,By.XPATH,self.virtual_pin_input_xpath,timeout=20,condition="visible")
        vp_input_field.send_keys(text)

    def enter_amount_into_sale_amount(self,text):
        amount_field = wait_for_element(self.driver, By.XPATH, self.sale_amount_input_xpath, timeout=20,condition="visible")
        amount_field.send_keys(text)

    def verify_virtual_terminal_header_is_displayed(self):
        HomePage(self.driver).waiting_for_js_loader_to_disappear()
        vt_header = wait_for_element(self.driver,By.XPATH,self.virtual_terminal_header_xpath,timeout=20,condition="visible")
        return vt_header.is_displayed()