import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utilities import ReadConfigurations
from utilities.wait_helpers import wait_for_element

# Helper function to initialize the driver
def initialize_driver():
    browser = ReadConfigurations.read_configuration("browser and url", "browser")
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Provide a valid browser name from this list: chrome/firefox/edge")

    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("browser and url", "url")
    driver.get(app_url)
    return driver

# Fixture to log screenshot on failure
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)

# Hook to attach test result to the item
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

# Generic setup and teardown fixture
@pytest.fixture(scope="function")
def setup_and_teardown(request):
    global driver
    driver = initialize_driver()
    login_page = LoginPage(driver)
    login_page.waiting_for_js_loader_to_disappear()
    login_page.verify_login_page_LUT_logo_is_displayed()
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()

# Setup and login fixture
@pytest.fixture(scope="function")
def setup_and_teardown_login(request):
    global driver
    driver = initialize_driver()
    login_page = LoginPage(driver)
    login_page.waiting_for_js_loader_to_disappear()
    login_page.verify_login_page_LUT_logo_is_displayed()
    login_page.login_to_application("bankdata2@gmail.com","Admin@123")
    home_page = HomePage(driver)
    home_page.waiting_for_js_loader_to_disappear()
    home_page.verify_settlement_summary_widget_is_displayed()
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()