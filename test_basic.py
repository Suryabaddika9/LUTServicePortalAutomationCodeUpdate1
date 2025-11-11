"""
#import time

#def test_service_portal_login_page():

  #  from selenium import webdriver
   # driver = webdriver.Firefox()
    #driver.get("https://myportal.stage-orlando.payresults.ai/")
    #driver.maximize_window()
    #time.sleep(5)
    #driver.quit





import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import allure
from allure_commons.types import AttachmentType

from utilities import ReadConfigurations
from utilities.wait_helpers import wait_for_element


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function",params=["chrome","firefox","edge"])
def setup_and_teardown(request):

    To run the tests across all browsers, runs each test case in all 3 browsers.
        if request.param=="chrome":
            driver = webdriver.Chrome()
        elif request.param=="firefox":
            driver = webdriver.Firefox()
        elif request.param=="edge":
            driver = webdriver.Edge()


    browser = ReadConfigurations.read_configuration("browser and url", "browser")
    global driver
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("browser and url", "url")
    driver.get(app_url)
    driver.maximize_window()
    JS_loader = wait_for_element(driver, By.CSS_SELECTOR, "div.loaderContainer", timeout=30, condition="invisible")
    login_page_LUT_logo = wait_for_element(driver, By.XPATH, "//img[@alt='Logo']", timeout=30, condition="visible")
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()


@pytest.fixture(scope="function")  #@pytest.fixture(scope="function",params=["chrome","firefox","edge"])
def setup_and_teardown_login(request):



    To run the tests across all browsers, runs each test case in all 3 browsers.
    if request.param=="chrome":
        driver = webdriver.Chrome()
    elif request.param=="firefox":
        driver = webdriver.Firefox()
    elif request.param=="edge":
        driver = webdriver.Edge()

    browser=ReadConfigurations.read_configuration("browser and url", "browser")
    global driver
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("browser and url", "url")
    driver.get(app_url)
    login_page_LUT_logo = wait_for_element(driver, By.XPATH, "//img[@alt='Logo']", timeout=30, condition="visible")
    driver.find_element(By.XPATH, "//input[@id='emailInput']").send_keys("bankdata2@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='passwordInput']").send_keys("Admin@123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # Wait until loader disappears
    js_loader = wait_for_element(driver, By.CSS_SELECTOR, "div.loaderContainer", timeout=20, condition="invisible")
    home_page_widget = wait_for_element(driver, By.XPATH, "//div[@class='widget-title']", timeout=30, condition="visible")
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()
"""




"""

from faker import Faker
def test_faker():
    fake = Faker()
    fake = Faker()
    print(fake.name(), fake.email())

def test_faker_indian():
    fake = Faker()
    fake = Faker()
    fake = Faker('en_IN')  # For Indian names, addresses, etc.
    print(fake.name())
    print(fake.phone_number())
    
   """
#for chrome

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set download directory
download_dir = "/path/to/download"

chrome_options = Options()
prefs = {
    "download.default_directory": download_dir,  # Set download folder
    "download.prompt_for_download": False,       # Disable download prompt
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True                # Avoid security blocks
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize driver
service = Service("/path/to/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

#for firefox

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

download_dir = "/path/to/download"

options = Options()
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)  # Use custom folder
profile.set_preference("browser.download.dir", download_dir)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/octet-stream")  # MIME types
profile.set_preference("pdfjs.disabled", True)  # Disable PDF viewer

driver = webdriver.Firefox(firefox_profile=profile, options=options)
driver.get("https://example.com/file.pdf")
