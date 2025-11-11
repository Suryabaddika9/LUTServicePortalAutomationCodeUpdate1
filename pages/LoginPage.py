from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from utilities.wait_helpers import wait_for_element


class LoginPage:

    def __init__(self,driver):
        self.driver = driver


    js_loader_css_selector = "div.loaderContainer"
    login_page_LUT_logo_xpath = "//img[@alt='Logo']"
    email_field_xpath = "//input[@id='emailInput']"
    password_field_xpath = "//input[@id='passwordInput']"
    login_button_xpath = "//button[@type='submit']"
    email_error_msg_xpath = "//span[@id='emailError']"
    password_error_msg_xpath = "//span[@id='passwordError']"
    invalid_user_alert_xpath = "//p[normalize-space()='User does not exist']"

    invalid_credentials_error_msg_xpath = "//p[normalize-space()='Invalid credentials']"

    def waiting_for_js_loader_to_disappear(self):
        return wait_for_element(self.driver, By.CSS_SELECTOR, self.js_loader_css_selector, timeout=20,condition="invisible")


    def verify_login_page_LUT_logo_is_displayed(self):
        logo = wait_for_element(self.driver,By.XPATH,self.login_page_LUT_logo_xpath,timeout=20,condition="visible")
        return logo.is_displayed()

    def enter_email_into_email_field(self,email):
        self.driver.find_element(By.XPATH,self.email_field_xpath).send_keys(email)

    def enter_password_into_password_field(self,password):
        self.driver.find_element(By.XPATH,self.password_field_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def login_to_application(self,email,password):
        self.enter_email_into_email_field(email)
        self.enter_password_into_password_field(password)
        self.click_login_button()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()

    def verify_email_error_msg_is_displayed(self):
        return self.driver.find_element(By.XPATH,self.email_error_msg_xpath).is_displayed()

    def verify_password_error_msg_is_displayed(self):
        return self.driver.find_element(By.XPATH,self.password_error_msg_xpath).is_displayed()

    def verify_invalid_user_alert_is_displayed(self):
        return self.driver.find_element(By.XPATH,self.invalid_user_alert_xpath).is_displayed()

    def verify_invalid_credentials_error_msg_is_displayed(self):
        return self.driver.find_element(By.XPATH,self.invalid_credentials_error_msg_xpath).is_displayed()