import time
from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.HomePage import HomePage
from utilities.wait_helpers import wait_for_element


def select_option_from_dropdown_menu(dropdown_menu, visible_text):
    #Create a Select object
    select = Select(dropdown_menu)
    time.sleep(3)

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
    pdf_file_xpath = "//div[contains(@role,'grid')]//div[2]//div[3]//div[1]//*[name()='svg']"
    table_component_xpath = "//div[@class='table-component ']"
    summary_reports_xpath = "//div[text()='Summary Reports']"
    deposits_and_fees_summary_reports_xpath = "//div[text()='Deposits and Fees Summary Report']"  #its not in DOM retrieved using AI tools
    detailed_reports_xpath = "//div[text()='Detailed Reports']"
    daily_sales_reports_xpath = "//div[text()='Daily Sales Reports']"



    def verify_table_component_is_displayed(self):
        return wait_for_element(self.driver,By.XPATH,self.table_component_xpath).is_displayed()


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

    def select_summary_reports_and_deposits_and_fee_summary_options_from_report_category(self):
        report_category_dropdown_menu = wait_for_element(self.driver,By.XPATH,self.report_category_select_dropdown_menu_xpath)
        report_category_dropdown_menu.click()
        summary_reports_option  = wait_for_element(self.driver,By.XPATH,self.summary_reports_xpath,timeout=5,condition="visible")
        summary_reports_option.click()
        time.sleep(3)
        report_type_dropdown_menu = wait_for_element(self.driver,By.XPATH,self.report_type_select_dropdown_menu_xpath,timeout=5,condition="visible")
        report_type_dropdown_menu.click()
        deposits_and_fee_summary_reports_option = wait_for_element(self.driver, By.XPATH, self.deposits_and_fees_summary_reports_xpath, timeout=10,
                                                  condition="visible")
        deposits_and_fee_summary_reports_option.click()

    def select_detailed_reports_and_daily_sales_reports_options_from_report_category(self):
        report_category_dropdown_menu = wait_for_element(self.driver, By.XPATH,
                                                         self.report_category_select_dropdown_menu_xpath)
        report_category_dropdown_menu.click()
        detailed_reports_option = wait_for_element(self.driver, By.XPATH, self.detailed_reports_xpath, timeout=5,
                                                  condition="visible")
        detailed_reports_option.click()
        time.sleep(3)
        report_type_dropdown_menu = wait_for_element(self.driver, By.XPATH, self.report_type_select_dropdown_menu_xpath,
                                                     timeout=5, condition="visible")
        report_type_dropdown_menu.click()
        daily_sales_reports_option = wait_for_element(self.driver, By.XPATH, self.daily_sales_reports_xpath, timeout=5,condition="visible")
        daily_sales_reports_option.click()

    def download_summary_reports_and_deposits_and_fee_summary_options_from_report_category(self):
        report_category_dropdown_menu = wait_for_element(self.driver,By.XPATH,self.report_category_select_dropdown_menu_xpath)
        report_category_dropdown_menu.click()
        summary_reports_option  = wait_for_element(self.driver,By.XPATH,self.summary_reports_xpath,timeout=5,condition="visible")
        summary_reports_option.click()
        time.sleep(3)
        report_type_dropdown_menu = wait_for_element(self.driver,By.XPATH,self.report_type_select_dropdown_menu_xpath,timeout=5,condition="visible")
        report_type_dropdown_menu.click()
        deposits_and_fee_summary_reports_option = wait_for_element(self.driver, By.XPATH, self.deposits_and_fees_summary_reports_xpath, timeout=10,condition="visible")
        deposits_and_fee_summary_reports_option.click()

        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        time.sleep(3)
        pdf = wait_for_element(self.driver,By.XPATH,self.pdf_file_xpath,timeout=10,condition="clickable")
        pdf.click()
        home_page.waiting_for_js_loader_to_disappear()

    def download_detailed_reports_and_daily_sales_reports_options_from_report_category(self):
        report_category_dropdown_menu = wait_for_element(self.driver, By.XPATH,
                                                         self.report_category_select_dropdown_menu_xpath)
        report_category_dropdown_menu.click()
        detailed_reports_option = wait_for_element(self.driver, By.XPATH, self.detailed_reports_xpath, timeout=5,condition="visible")
        detailed_reports_option.click()
        time.sleep(3)
        report_type_dropdown_menu = wait_for_element(self.driver, By.XPATH, self.report_type_select_dropdown_menu_xpath,timeout=5, condition="visible")
        report_type_dropdown_menu.click()
        daily_sales_reports_option = wait_for_element(self.driver, By.XPATH,self.daily_sales_reports_xpath,timeout=10,condition="visible")
        daily_sales_reports_option.click()

        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        time.sleep(3)
        pdf = wait_for_element(self.driver,By.XPATH,self.pdf_file_xpath,timeout=10,condition="clickable")
        pdf.click()
        home_page.waiting_for_js_loader_to_disappear()








