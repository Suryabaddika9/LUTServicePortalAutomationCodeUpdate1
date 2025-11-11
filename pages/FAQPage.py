import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.HomePage import HomePage
from utilities.wait_helpers import wait_for_element, wait_for_elements


class FAQPage:

    def __init__(self,driver):
        self.driver = driver

    FAQ_sidebar_with_options_xpath = "//div[@class='sidebar']"
    close_option_xpath = "//span[@class='close-text']"
    left_number_of_FAQs_displayed_xpath = "//div[@class='sidebar-title']"
    right_number_of_FAQs_displayed_xpath = "//h2[@class='section-name ']"


    def verify_FAQ_sidebar_with_options_is_displayed(self):
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        side_bar = wait_for_element(self.driver,By.XPATH,self.FAQ_sidebar_with_options_xpath,timeout=10,condition="visible")
        return side_bar.is_displayed()

    def click_on_close_option(self):
        close_option = wait_for_element(self.driver,By.XPATH,self.close_option_xpath,timeout=20,condition="clickable")
        close_option.click()

    def left_number_of_FAQ_questions(self):
        HomePage(self.driver).waiting_for_js_loader_to_disappear()
        left = self.driver.find_elements(By.XPATH, self.left_number_of_FAQs_displayed_xpath)
        return len(left)

    def right_number_of_FAQ_questions(self):
        HomePage(self.driver).waiting_for_js_loader_to_disappear()
        right = self.driver.find_elements(By.XPATH, self.right_number_of_FAQs_displayed_xpath)
        return len(right)