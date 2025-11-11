from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.wait_helpers import wait_for_element




from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def select_option_from_custom_dropdown(driver, dropdown_locator, option_text):
    # Click dropdown to open options
    dropdown = wait_for_element(driver,By.XPATH,dropdown_locator,timeout=20,condition="clickable")
    dropdown.click()

    # Click the option by visible text
    option_locator = (By.XPATH, f"//li[normalize-space()='{option_text}']")

    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(option_locator)
    )
    option.click()






def select_option_from_dropdown_menu(dropdown_menu, visible_text):
    # Create a Select object
    select = Select(dropdown_menu)
    # 1️⃣ Select by visible text
    select.select_by_visible_text(visible_text)


class MyReportsPage:

    def __init__(self,driver):
        self.driver = driver

    report_category_option_xpath = "//label[normalize-space()='Report Category']"
    report_category_select_dropdown_menu_xpath = "//div[@class='selectField__value-container css-hlgwow']//div[@class='selectField__input-container css-19bb58m']"

    report_type_option_xpath = "//label[normalize-space()='Report Type']"
    report_type_select_dropdown_menu_xpath = "//div[@class='selectField__value-container css-hlgwow']//div[@class='selectField__input-container css-19bb58m']"
    no_data_logo_xpath = "//div[@class='initial-msg']//*[name()='svg']"
    no_data_text_xpath = "//h1[normalize-space()='No Data']"

    def verify_no_data_logo_and_text_are_displayed(self):
        no_data_logo = wait_for_element(self.driver,By.XPATH,self.no_data_logo_xpath)
        no_data_text = wait_for_element(self.driver,By.XPATH,self.no_data_text_xpath)
        return no_data_logo.is_displayed() and no_data_text.is_displayed()

    def verify_report_category_option_is_displayed(self):
        rc_opt = wait_for_element(self.driver,By.XPATH,self.report_category_option_xpath)
        return rc_opt.is_displayed()

    def verify_report_type_option_is_displayed(self):
        rt_opt = wait_for_element(self.driver,By.XPATH,self.report_type_option_xpath)
        return rt_opt.is_displayed()

    def verify_report_category_and_report_type_options_are_displayed(self):
        return self.verify_report_type_option_is_displayed() and self.verify_report_category_option_is_displayed()

    def select_summary_reports_option_from_report_category(self):
        dropdown_menu = wait_for_element(self.driver,By.XPATH,self.report_category_select_dropdown_menu_xpath)
        visible_text = "Summary Reports"
        select_option_from_dropdown_menu(dropdown_menu, visible_text)
