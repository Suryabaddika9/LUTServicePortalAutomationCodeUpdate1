from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from utilities.wait_helpers import wait_for_element


class AccountSettingsPage:

    def __init__(self,driver):
        self.driver = driver

    close_option_css_selector = ".close-text"
    profile_and_settings_text_xpath = "//p[@class='title']"

    def verify_profile_and_settings_text_is_displayed(self):
        text = wait_for_element(self.driver,By.XPATH, self.profile_and_settings_text_xpath,timeout=10,condition="visible")
        return text.is_displayed()

    def click_on_close_option(self):
        close = wait_for_element(self.driver,By.CSS_SELECTOR,self.close_option_css_selector,timeout=10,condition="visible")
        close.click()

