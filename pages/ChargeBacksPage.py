from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from utilities.wait_helpers import wait_for_element


class ChargeBacksPage:

    def __init__(self,driver):
        self.driver = driver

    charge_backs_widget_heading_xpath = "//div[@class='widget-title']"
    unresolved_charge_backs_kpi_xpath = "//span[contains(text(),'UNRESOLVED')]"
    new_charge_backs_kpi_xpath = "//span[normalize-space()='NEW CHARGEBACKS']"
    filters_widget_xpath = "//div[@class='right-col-left col']"
    filters_status_dropdown_option_xpath = "//label[normalize-space()='Status']"
    filters_time_frame_dropdown_option_xpath = "//label[normalize-space()='Time Frame']"
    filters_card_types_dropdown_option_xpath = "//label[normalize-space()='Card Types']"
    filters_reason_dropdown_option_xpath = "//label[normalize-space()='Reason']"
    filters_transaction_id_option_xpath = "//label[@for='transactionSearch']"
    charge_backs_table_container_xpath = "//div[@role='grid']"

    def verify_charge_backs_table_container_is_displayed(self):
        table = wait_for_element(self.driver,By.XPATH,self.charge_backs_table_container_xpath)
        return table.is_displayed()

    def verify_all_filter_options_are_available(self):
        return (self.verify_filers_status_option_is_displayed()
                and self.verify_filters_time_frame_option_is_displayed()
                and self.verify_filters_card_types_option_is_displayed()
                and self.verify_filters_reason_option_is_displayed()
                and self.verify_filters_transaction_id_option_is_displayed())

    def verify_filters_transaction_id_option_is_displayed(self):
        tran_id_opt = wait_for_element(self.driver, By.XPATH, self.filters_transaction_id_option_xpath)
        return tran_id_opt.is_displayed()

    def verify_filters_reason_option_is_displayed(self):
        reason_opt = wait_for_element(self.driver, By.XPATH, self.filters_reason_dropdown_option_xpath)
        return reason_opt.is_displayed()

    def verify_filters_card_types_option_is_displayed(self):
        card_types_opt = wait_for_element(self.driver, By.XPATH, self.filters_card_types_dropdown_option_xpath)
        return card_types_opt.is_displayed()

    def verify_filters_time_frame_option_is_displayed(self):
        time_frame_opt = wait_for_element(self.driver, By.XPATH, self.filters_time_frame_dropdown_option_xpath)
        return time_frame_opt.is_displayed()

    def verify_filers_status_option_is_displayed(self):
        status_opt = wait_for_element(self.driver,By.XPATH,self.filters_status_dropdown_option_xpath)
        return status_opt.is_displayed()

    def verify_filters_widget_is_displayed(self):
        filters_wid = wait_for_element(self.driver,By.XPATH,self.filters_widget_xpath)
        return filters_wid.is_displayed()

    def verify_new_charge_backs_kpi_is_displayed(self):
        new_cb_kpi = wait_for_element(self.driver,By.XPATH,self.new_charge_backs_kpi_xpath)
        return new_cb_kpi.is_displayed()

    def verify_unresolved_charge_backs_kpi_is_displayed(self):
        unresolved_cb_kpi = wait_for_element(self.driver,By.XPATH,self.unresolved_charge_backs_kpi_xpath)
        return unresolved_cb_kpi.is_displayed()

    def verify_charge_backs_widget_heading_is_displayed(self):
        cb_head = wait_for_element(self.driver,By.XPATH,self.charge_backs_widget_heading_xpath,timeout=10,condition="visible")
        return cb_head.is_displayed()
