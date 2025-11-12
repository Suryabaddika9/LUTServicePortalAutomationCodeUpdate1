import allure
import pytest
import time

from pages.AccountSettingsPage import AccountSettingsPage
from pages.ChargeBacksPage import ChargeBacksPage
from pages.MerchantSettingsPage import MerchantSettingsPage
from pages.MyReportsPage import MyReportsPage
from utilities import wait_utils, open_file_and_read
from utilities.open_file_and_read import open_file, read_pdf_text
from utilities.wait_helpers import wait_for_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.HomePage import HomePage
from pages.TransactionPage import TransactionPage
from pages.VirtualTerminalPage import VirtualTerminalPage
from utilities.wait_utils import wait_for_file



@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("setup_and_teardown_login","log_on_failure")
class TestLUTServicePortalMyReportsFunctionality:
    driver = None

    def navigate_to_my_reports_option(self):
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        home_page.click_on_my_reports_option()
        home_page.waiting_for_js_loader_to_disappear()

    def test_verify_report_category_report_type_options_are_displayed(self):
        self.navigate_to_my_reports_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        my_reports_page = MyReportsPage(self.driver)
        assert my_reports_page.verify_report_category_and_report_type_options_are_displayed()

    def test_verify_no_data_logo_and_text_are_displayed(self):
        self.navigate_to_my_reports_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        my_reports_page = MyReportsPage(self.driver)
        assert my_reports_page.verify_no_data_logo_and_text_are_displayed()

    def test_verify_summary_reports_and_deposits_and_fee_summary_in_report_category_and_type(self):
        self.navigate_to_my_reports_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        my_reports_page = MyReportsPage(self.driver)
        my_reports_page.select_summary_reports_and_deposits_and_fee_summary_options_from_report_category()
        assert my_reports_page.verify_table_component_is_displayed()

    def test_verify_detailed_reports_and_daily_sales_reports_in_report_category_and_type(self):
        self.navigate_to_my_reports_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        my_reports_page = MyReportsPage(self.driver)
        my_reports_page.select_detailed_reports_and_daily_sales_reports_options_from_report_category()
        assert my_reports_page.verify_table_component_is_displayed()

    def test_file_download_for_summary_reports_deposits_and_fee_summary_in_report_category_and_type(self,download_dir):
        self.navigate_to_my_reports_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        my_reports_page = MyReportsPage(self.driver)
        my_reports_page.download_summary_reports_and_deposits_and_fee_summary_options_from_report_category()
        time.sleep(3)
        assert wait_for_file(download_dir), "Download failed / No file found"

    def test_open_downloaded_file_for_summary_reports_deposits_and_fee_summary_in_report_category(self,download_dir):
        self.navigate_to_my_reports_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        my_reports_page = MyReportsPage(self.driver)
        my_reports_page.download_summary_reports_and_deposits_and_fee_summary_options_from_report_category()
        time.sleep(3)
        #assert wait_for_file(download_dir), "Download failed / No file found"
        fpath = wait_for_file(download_dir, pattern="*.pdf", timeout=60, stable_seconds=1)
        # Assert file exists and not empty
        assert fpath.exists(), "File was not downloaded"
        assert fpath.stat().st_size > 0, "File is empty"
        print(f"\nDownloaded PDF File Path: {fpath}\n")
        # ---- OPEN THE FILE LOCALLY (optional, only works on machines with GUI) ----
        #open_file(str(fpath))
        # ---- READ THE PDF TEXT ----
        text = read_pdf_text(str(fpath))
        print("\n===== PDF CONTENT START =====")
        print(text)  # print first 500 chars
        print("===== PDF CONTENT END =====\n")
        # ---- ASSERT THAT EXPECTED CONTENT EXISTS ----
        # Change this to what you expect inside the PDF:
        assert "Deposit" in text or "Fee" in text, "Expected text not found in PDF"

    def test_file_download_for_detailed_reports_and_daily_sales_reports_in_report_category_and_type(self,download_dir):
        self.navigate_to_my_reports_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        my_reports_page = MyReportsPage(self.driver)
        my_reports_page.download_detailed_reports_and_daily_sales_reports_options_from_report_category()
        time.sleep(3)
        assert wait_for_file(download_dir), "Download failed / No file found"

    def test_open_downloaded_file_for_detailed_reports_and_daily_sales_reports_in_report_category_and_type(self,download_dir):
        self.navigate_to_my_reports_option()
        home_page = HomePage(self.driver)
        home_page.waiting_for_js_loader_to_disappear()
        my_reports_page = MyReportsPage(self.driver)
        my_reports_page.download_detailed_reports_and_daily_sales_reports_options_from_report_category()
        time.sleep(3)
        #assert wait_for_file(download_dir), "Download failed / No file found"
        fpath = wait_for_file(download_dir, pattern="*.pdf", timeout=60, stable_seconds=1)
        # Assert file exists and not empty
        assert fpath.exists(), "File was not downloaded"
        assert fpath.stat().st_size > 0, "File is empty"
        print(f"\nDownloaded PDF File Path: {fpath}\n")
        # ---- OPEN THE FILE LOCALLY (optional, only works on machines with GUI) ----
        #open_file(str(fpath))
        # ---- READ THE PDF TEXT ----
        text = read_pdf_text(str(fpath))
        print("\n===== PDF CONTENT START =====")
        print(text)  # print first 500 chars
        print("===== PDF CONTENT END =====\n")
        # ---- ASSERT THAT EXPECTED CONTENT EXISTS ----
        # Change this to what you expect inside the PDF:
        assert "Deposit" in text or "Fee" in text, "Expected text not found in PDF"