from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from utilities.wait_helpers import wait_for_element


class AccountSettingsPage:

    def __init__(self,driver):
        self.driver = driver

    close_option_css_selector = ".close-text"
    profile_and_settings_text_xpath = "//p[@class='title']"
    update_info_link_xpath = "//a[@class='header-link']"
    personal_info_popup_xpath = "//h5[@class='modal-title']//p[contains(text(),'Personal Information')]"
    popup_close_opt_xpath = "//h5[@class='modal-title']//div//*[name()='svg']"
    change_email_link_xpath = "//p[normalize-space()='change email']"
    change_my_email_popup_xpath = "//p[normalize-space()='Change my Email']"
    change_password_link_xpath = "//p[normalize-space()='change password']"
    change_my_password_popup_xpath = "//p[normalize-space()='Change my Password']"
    change_password_button_in_popup_xpath = "//button[normalize-space()='Change Password']"
    error_field_text_in_popup_xpath = "//p[@class='error-field']"

    def verify_error_field_text_in_popup_is_displayed(self):
        return wait_for_element(self.driver,By.XPATH,self.error_field_text_in_popup_xpath,timeout=10,condition="visible").is_displayed()

    def click_on_change_password_button_in_popup(self):
        wait_for_element(self.driver,By.CSS_SELECTOR,"div.modal.fade.show",timeout=10,condition="invisible")
        button = wait_for_element(self.driver,By.XPATH,self.change_password_button_in_popup_xpath,timeout=10,condition="clickable")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)


    def verify_change_my_password_popup_is_displayed(self):
        return wait_for_element(self.driver,By.XPATH,self.change_my_password_popup_xpath,timeout=10,condition="visible").is_displayed()

    def click_on_change_password_link(self):
        wait_for_element(self.driver,By.XPATH,self.change_password_link_xpath).click()

    def verify_change_my_mail_popup_is_displayed(self):
        return wait_for_element(self.driver,By.XPATH,self.change_my_email_popup_xpath,timeout=10,condition="visible").is_displayed()

    def click_on_change_email_link(self):
        wait_for_element(self.driver,By.XPATH,self.change_email_link_xpath).click()

    def click_on_popup_close_option(self):
        wait_for_element(self.driver,By.XPATH,self.popup_close_opt_xpath).click()

    def verify_personal_info_popup_is_displayed(self):
        return wait_for_element(self.driver,By.XPATH,self.personal_info_popup_xpath,timeout=10,condition="visible").is_displayed()

    def click_on_update_info_link(self):
        wait_for_element(self.driver,By.XPATH,self.update_info_link_xpath).click()

    def verify_profile_and_settings_text_is_displayed(self):
        text = wait_for_element(self.driver,By.XPATH, self.profile_and_settings_text_xpath,timeout=10,condition="visible")
        return text.is_displayed()

    def click_on_close_option(self):
        close = wait_for_element(self.driver,By.CSS_SELECTOR,self.close_option_css_selector,timeout=10,condition="visible")
        close.click()

