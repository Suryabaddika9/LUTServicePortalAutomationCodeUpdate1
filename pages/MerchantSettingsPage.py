from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from utilities.scroll_and_click_button import scroll_and_click_button
from utilities.wait_helpers import wait_for_element


class MerchantSettingsPage:

    def __init__(self,driver):
        self.driver = driver

    merchant_settings_text_xpath = "//p[@class='merchant-profile-header-title']"
    close_option_css_selector = ".close-text"
    update_info_link_xpath = "//span[normalize-space()='update info']"
    business_info_popup_xpath = "//p[normalize-space()='Business Information']"
    close_popup_xpath = "//h5[@class='modal-title']//div//*[name()='svg']"
    financial_info_and_pricing_option_xpath = "//a[normalize-space()='Financial Information & Pricing']"
    financial_info_popup_xpath = "//p[normalize-space()='Financial Information']"
    tips_and_processing_fee_option_xpath = "//a[normalize-space()='Tips & Processing Fees']"
    instore_tipping_option_xpath = "//p[normalize-space()='In-Store Tipping Option']"
    instore_processing_fee_option_xpath = "//p[normalize-space()='In-Store Processing Fee Option']"
    online_shopping_option_xpath = "//a[normalize-space()='Online Shopping']"
    lut_buy_now_text_xpath = "//p[normalize-space()='Lüt BuyNow']"
    lut_orders_text_xpath = "//p[normalize-space()='Lüt Orders']"
    manage_users_option_xpath = "//a[normalize-space()='Manage Users']"
    name_text_in_manage_users_xpath = "//div[normalize-space()='Name']"
    add_user_button_in_manage_users_xpath = "//button[@class='addUser-button']"
    add_user_popup_text_xpath = "//p[normalize-space()='Add User']"
    add_user_button_in_popup_xpath = "//div[@class='footer-contents']/button[@type='button']"
    warning_msg_about_all_fields_xpath = "//p[@class='generic-error-message']"
    email_field_in_add_user_popup = "//input[@id='input-email']"
    phone_num_field_in_add_user_popup = "//input[@id='phone-number-input']"
    email_field_warning_msg_xpath = "//div[@class='error-field']"
    phone_num_filed_warning_msg_xpath = "//div[@class='error-field d-block invalid-feedback']"
    manage_locations_option_xpath = "//a[normalize-space()='Manage Locations']"
    no_locations_available_text = "//p[normalize-space()='No Locations Available']"
    add_location_button_in_manage_locations_xpath = "//span[@class='close-text add-Location-button']"
    add_location_popup_text_xpath = "//p[normalize-space()='Add a Location']"

    def verify_add_location_popup_text_is_displayed(self):
        return wait_for_element(self.driver, By.XPATH, self.add_location_popup_text_xpath, timeout=10, condition="visible").is_displayed()

    def click_on_add_location_button_in_manage_locations_option(self):
        wait_for_element(self.driver,By.XPATH,self.add_location_button_in_manage_locations_xpath,timeout=10,condition="visible").click()

    def verify_no_locations_available_text_is_displayed(self):
        return wait_for_element(self.driver, By.XPATH, self.no_locations_available_text, timeout=10, condition="visible").is_displayed()

    def click_on_manage_locations_option(self):
        wait_for_element(self.driver, By.XPATH, self.manage_locations_option_xpath, timeout=10,condition="visible").click()

    def verify_email_and_phone_num_warning_msg_are_displayed(self):
        email_warning = wait_for_element(self.driver,By.XPATH,self.email_field_warning_msg_xpath,timeout=10,condition="visible").is_displayed()
        phone_num_warning = wait_for_element(self.driver,By.XPATH,self.phone_num_filed_warning_msg_xpath,timeout=10,condition="visible").is_displayed()
        return email_warning and phone_num_warning

    def click_on_phone_num_field_in_add_user_popup(self):
        wait_for_element(self.driver,By.XPATH,self.phone_num_field_in_add_user_popup,timeout=10,condition="visible").click()

    def click_on_email_field_in_add_user_popup(self):
        wait_for_element(self.driver,By.XPATH,self.email_field_in_add_user_popup,timeout=10,condition="visible").click()

    def verify_warning_msg_about_all_fields_in_add_user_popup_is_displayed(self):
        return wait_for_element(self.driver,By.XPATH,self.warning_msg_about_all_fields_xpath,timeout=10,condition="visible").is_displayed()

    def click_on_add_user_button_in_popup(self):
        scroll_and_click_button(self.driver,By.XPATH,self.add_user_button_in_popup_xpath,timeout=20)
        #wait_for_element(self.driver,By.XPATH,self.add_user_button_in_popup_xpath,timeout=10,condition="visible").click()

    def verify_add_user_text_is_displayed_in_add_user_popup(self):
        return wait_for_element(self.driver,By.XPATH,self.add_user_popup_text_xpath,timeout=10,condition="visible").is_displayed()

    def click_on_add_user_button(self):
        wait_for_element(self.driver,By.XPATH,self.add_user_button_in_manage_users_xpath,timeout=10,condition="visible").click()

    def verify_name_is_displayed_in_manage_users(self):
        return wait_for_element(self.driver,By.XPATH,self.name_text_in_manage_users_xpath,timeout=10,condition="visible").is_displayed()

    def click_on_manage_users_option(self):
        wait_for_element(self.driver,By.XPATH,self.manage_users_option_xpath,timeout=10,condition="visible").click()

    def verify_lut_buy_now_and_lut_orders_texts_are_displayed(self):
        lut_buy_now = wait_for_element(self.driver,By.XPATH,self.lut_buy_now_text_xpath,timeout=10,condition="visible").is_displayed()
        lut_orders = wait_for_element(self.driver,By.XPATH,self.lut_orders_text_xpath,timeout=10,condition="visible").is_displayed()
        return lut_buy_now and lut_orders

    def click_on_online_shopping_option(self):
        wait_for_element(self.driver,By.XPATH,self.online_shopping_option_xpath,timeout=10,condition="visible").click()

    def verify_instore_tipping_and_processing_fee_options_are_displayed(self):
        inst_tipping = wait_for_element(self.driver,By.XPATH,self.instore_tipping_option_xpath,timeout=10,condition="visible").is_displayed()
        inst_proc_fee = wait_for_element(self.driver,By.XPATH,self.instore_processing_fee_option_xpath,timeout=10,condition="visible").is_displayed()
        return inst_tipping and inst_proc_fee

    def click_on_tips_and_processing_fee_option(self):
        wait_for_element(self.driver,By.XPATH,self.tips_and_processing_fee_option_xpath,timeout=10,condition="visible").click()

    def verify_financial_info_popup_is_displayed(self):
        return wait_for_element(self.driver,By.XPATH,self.financial_info_popup_xpath,timeout=10,condition="visible").is_displayed()

    def click_on_financial_info_and_pricing_option(self):
        wait_for_element(self.driver,By.XPATH,self.financial_info_and_pricing_option_xpath,timeout=10,condition="clickable").click()

    def click_on_close_popup_option(self):
        wait_for_element(self.driver,By.XPATH,self.close_popup_xpath,timeout=10,condition="clickable").click()

    def verify_business_info_popup_is_displayed(self):
        return wait_for_element(self.driver,By.XPATH,self.business_info_popup_xpath,timeout=10,condition="visible").is_displayed()

    def click_on_update_info_link(self):
        wait_for_element(self.driver,By.XPATH,self.update_info_link_xpath,timeout=10,condition="clickable").click()

    def click_on_close_option(self):
        close = wait_for_element(self.driver,By.CSS_SELECTOR, self.close_option_css_selector,timeout=10,condition="visible")
        close.click()

    def verify_merchant_settings_text_is_displayed(self):
        mer_set_text = wait_for_element(self.driver,By.XPATH,self.merchant_settings_text_xpath,timeout=10,condition="visible")
        return mer_set_text.is_displayed()




