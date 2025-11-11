from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from utilities.wait_helpers import wait_for_element


class MyReportsPage:

    def __init__(self,driver):
        self.driver = driver

    report_category_option_xpath = "//label[normalize-space()='Report Category']"
    report_category_select_dropdown_menu_xpath = "//div[@class='selectField__value-container css-hlgwow']//div[@class='selectField__input-container css-19bb58m']"

    report_type_option_xpath = "//label[normalize-space()='Report Type']"
    report_type_select_dropdown_menu_xpath = "//div[@class='selectField__value-container css-hlgwow']//div[@class='selectField__input-container css-19bb58m']"