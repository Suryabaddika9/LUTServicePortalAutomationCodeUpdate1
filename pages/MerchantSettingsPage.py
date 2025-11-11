from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from utilities.wait_helpers import wait_for_element


class MerchantSettingsPage:

    def __init__(self,driver):
        self.driver = driver

    merchant_settings_text_xpath = "//p[@class='merchant-profile-header-title']"
    close_option_css_selector = ".close-text"


    def click_on_close_option(self):
        close = wait_for_element(self.driver,By.CSS_SELECTOR, self.close_option_css_selector,timeout=10,condition="visible")
        close.click()

    def verify_merchant_settings_text_is_displayed(self):
        mer_set_text = wait_for_element(self.driver,By.XPATH,self.merchant_settings_text_xpath,timeout=10,condition="visible")
        return mer_set_text.is_displayed()




