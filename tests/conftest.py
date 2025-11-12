# conftest.py  (keep your imports as-is)
import time
import pytest
import allure
from pathlib import Path

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utilities import ReadConfigurations



# ----------------- keep this global; your code uses it -----------------
driver = None

# ----------------- unchanged hook & failure logger -----------------
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if getattr(item, "rep_call", None) and item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)

# ----------------- NEW: per-test download dir -----------------
@pytest.fixture
def download_dir(tmp_path):
    return tmp_path  # pytest creates it; unique per test

# ----------------- SAME NAME: initialize_driver, now supports downloads -----------------
def initialize_driver(download_dir: Path | None = None):
    """
    Creates the WebDriver. If download_dir is provided, configures silent downloads.
    Name kept the same for compatibility.
    """
    browser = ReadConfigurations.read_configuration("browser and url", "browser").strip().lower()
    app_url = ReadConfigurations.read_configuration("browser and url", "url")
    headless_cfg = (ReadConfigurations.read_configuration("browser and url", "headless") or "false").strip().lower() == "true"

    global driver

    if browser == "chrome":
        options = ChromeOptions()
        if headless_cfg:
            options.add_argument("--headless=new")

        if download_dir is not None:
            prefs = {
                "download.default_directory": str(download_dir.resolve()),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
            }
            options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=options)

        # Allow downloads in headless Chrome/Edge via CDP
        if download_dir is not None:
            try:
                driver.execute_cdp_cmd(
                    "Page.setDownloadBehavior",
                    {"behavior": "allow", "downloadPath": str(download_dir.resolve())},
                )
            except Exception:
                pass

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless_cfg:
            options.add_argument("-headless")

        if download_dir is not None:
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.dir", str(download_dir.resolve()))
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.useDownloadDir", True)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference(
                "browser.helperApps.neverAsk.saveToDisk",
                ",".join([
                    "application/pdf",
                    "application/octet-stream",
                    "text/csv",
                    "application/vnd.ms-excel",
                    "application/zip",
                ])
            )
            profile.set_preference("pdfjs.disabled", True)
            driver = webdriver.Firefox(options=options, firefox_profile=profile)
        else:
            driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        if headless_cfg:
            options.add_argument("--headless=new")

        if download_dir is not None:
            prefs = {
                "download.default_directory": str(download_dir.resolve()),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
            }
            options.add_experimental_option("prefs", prefs)

        driver = webdriver.Edge(options=options)

        if download_dir is not None:
            try:
                driver.execute_cdp_cmd(
                    "Page.setDownloadBehavior",
                    {"behavior": "allow", "downloadPath": str(download_dir.resolve())},
                )
            except Exception:
                pass
    else:
        raise ValueError("Provide a valid browser name from this list: chrome/firefox/edge")

    driver.maximize_window()
    driver.get(app_url)
    return driver

# ----------------- keep your fixtures, just pass download_dir when needed -----------------
@pytest.fixture(scope="function")
def setup_and_teardown(request):
    global driver
    driver = initialize_driver()  # no downloads needed here
    login_page = LoginPage(driver)
    login_page.waiting_for_js_loader_to_disappear()
    login_page.verify_login_page_LUT_logo_is_displayed()
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()

@pytest.fixture(scope="function")
def setup_and_teardown_login(request, download_dir):
    """
    Same name kept. Now provides a driver with download prefs enabled
    by passing download_dir into initialize_driver().
    """
    global driver
    driver = initialize_driver(download_dir=download_dir)  # <-- enables downloads
    login_page = LoginPage(driver)
    login_page.waiting_for_js_loader_to_disappear()
    login_page.verify_login_page_LUT_logo_is_displayed()
    login_page.login_to_application("bankdata2@gmail.com", "Admin@123")
    home_page = HomePage(driver)
    home_page.waiting_for_js_loader_to_disappear()
    home_page.verify_settlement_summary_widget_is_displayed()
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()
