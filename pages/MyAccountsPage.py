from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from utilities.wait_helpers import wait_for_element


class MyAccountsPage:

    def __init__(self,driver):
        self.driver = driver

    my_accounts_image_xpath = "//img[@alt='myAccounts']"
    next_button_xpath = "//div[@class='icon-container']//*[name()='svg']"


    def verify_my_accounts_image_is_displayed(self):
        my_accounts_image = wait_for_element(self.driver, By.XPATH, self.my_accounts_image_xpath, timeout=20, condition="visible")
        return my_accounts_image.is_displayed()

    def click_next_button(self):
        next_button = self.driver.find_element(By.XPATH,self.next_button_xpath)
        next_button.click()



