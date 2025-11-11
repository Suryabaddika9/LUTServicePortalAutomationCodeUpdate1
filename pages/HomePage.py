from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from utilities.wait_helpers import wait_for_element


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    js_loader_css_selector = "div.loaderContainer"
    Merchant_ID_xpath = "//span[contains(text(),'Merchant ID:')]"
    merchant_view_dropdown_xpath = "//div[@class='selectField__input-container css-19bb58m']"
    home_page_LUT_logo_xpath = "//div[@class='logo-wrapper']//*[name()='svg']"
    daily_settlement_summary_widget_xpath = "//div[@class='widget-title']"
    transaction_id_field_xpath = "//input[@placeholder='Transaction ID']"
    transaction_id_not_found_text_xpath = "//div[@class='id-notfound']"
    support_option_css_selector = "#support"
    service_tickets_option_xpath = "//p[normalize-space()='Service Tickets']"
    merchant_account_logo_xpath = "//div//div//span//span"
    virtual_terminal_option_xpath = "//button[normalize-space()='Virtual Terminal']"
    notification_icon_css_locator = ".notoficationIcon"
    notification_box_xpath = "//div[@class='notoficationBox']"
    FAQ_option_xpath = "//p[normalize-space()='FAQ']"
    contact_us_section_phone_option_css_selector = "body div p:nth-child(3)"
    contact_us_section_email_option_xpath = "//p[normalize-space()='care@mylut.com']"
    account_settings_option_xpath = "//button[normalize-space()='Account Settings']"
    merchant_settings_option_xpath = "//button[normalize-space()='Merchant Settings']"
    charge_backs_option_xpath = "//a[normalize-space()='Chargebacks']"
    my_reports_option_xpath = "//a[normalize-space()='My Reports']"

    def click_on_my_reports_option(self):
        mr_opt = wait_for_element(self.driver,By.XPATH,self.my_reports_option_xpath,timeout=20,condition="visible")
        mr_opt.click()

    def click_on_charge_backs_option(self):
        cb_option = wait_for_element(self.driver,By.XPATH,self.charge_backs_option_xpath,timeout=20,condition="visible")
        cb_option.click()

    def click_on_merchant_settings_option(self):
        mer_option = wait_for_element(self.driver,By.XPATH,self.merchant_settings_option_xpath,timeout=20,condition="visible")
        mer_option.click()

    def click_on_account_settings_option(self):
        acc_option = wait_for_element(self.driver,By.XPATH,self.account_settings_option_xpath,timeout=20,condition="visible")
        acc_option.click()

    def click_on_contact_us_section_email_option(self):
        email_option = wait_for_element(self.driver,By.XPATH,self.contact_us_section_email_option_xpath,timeout=20,condition="visible")
        email_option.click()

    def click_on_contactus_section_phone_option(self):
        phone_option = wait_for_element(self.driver,By.CSS_SELECTOR,self.contact_us_section_phone_option_css_selector,timeout=20,condition="visible")
        phone_option.click()

    def click_on_FAQ_option(self):
        FAQ_option = wait_for_element(self.driver,By.XPATH,self.FAQ_option_xpath,timeout=20,condition="clickable")
        FAQ_option.click()

    def waiting_for_js_loader_to_disappear(self):
        return wait_for_element(self.driver, By.CSS_SELECTOR, self.js_loader_css_selector, timeout=20,condition="invisible")

    def verify_merchant_id_is_displayed(self):
        Merchant_ID = wait_for_element(self.driver,By.XPATH,self.Merchant_ID_xpath,timeout=30,condition="visible")
        return Merchant_ID.is_displayed()

    def click_on_merchant_view_dropdown(self):
        merchant_view_dropdown = wait_for_element(self.driver,By.XPATH,self.merchant_view_dropdown_xpath,timeout=20,condition="clickable")
        merchant_view_dropdown.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()

    def verify_home_page_LUT_logo_is_displayed(self):
        home_page_LUT_logo = wait_for_element(self.driver,By.XPATH,self.home_page_LUT_logo_xpath,timeout=20,condition="visible")
        return home_page_LUT_logo.is_displayed()

    def verify_settlement_summary_widget_is_displayed(self):
        settlement_summary_widget = wait_for_element(self.driver,By.XPATH,self.daily_settlement_summary_widget_xpath,timeout=20,condition="visible")
        return settlement_summary_widget.is_displayed()

    def enter_text_into_transaction_ID_field(self, transaction_ID):
        transaction_ID_field = wait_for_element(self.driver,By.XPATH,self.transaction_id_field_xpath,timeout=20,condition="visible")
        transaction_ID_field.send_keys(transaction_ID)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()

    def verify_transaction_id_not_found_text_is_displayed(self):
        return self.driver.find_element(By.XPATH,self.transaction_id_not_found_text_xpath).is_displayed()

    def click_on_support_option(self):
        wait_for_element(self.driver,By.CSS_SELECTOR,self.support_option_css_selector,timeout=20,condition="clickable")
        self.driver.find_element(By.CSS_SELECTOR,self.support_option_css_selector).click()

    def click_on_service_tickets_option(self):
        wait_for_element(self.driver,By.XPATH,self.service_tickets_option_xpath,timeout=20,condition="clickable")
        self.driver.find_element(By.XPATH,self.service_tickets_option_xpath).click()

    def click_on_merchant_account_logo(self):
        acc_logo = wait_for_element(self.driver,By.XPATH,self.merchant_account_logo_xpath,timeout=20,condition="clickable")
        acc_logo.click()

    def click_on_virtual_terminal_option(self):
        vt_option = wait_for_element(self.driver,By.XPATH,self.virtual_terminal_option_xpath,timeout=20,condition="visible")
        vt_option.click()

    def click_on_notification_icon(self):
        notif_icon = wait_for_element(self.driver,By.CSS_SELECTOR,self.notification_icon_css_locator,timeout=20,condition="clickable")
        notif_icon.click()

    def verify_notification_box_is_displayed(self):
        notif_box = wait_for_element(self.driver,By.XPATH,self.notification_box_xpath,timeout=20,condition="visible")
        return notif_box.is_displayed()





