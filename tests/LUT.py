import time
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


@pytest.fixture()
def setup_and_teardown():
    from selenium import webdriver
    global driver
    driver = webdriver.Edge()
    driver.get("https://myportal.stage-orlando.payresults.ai/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 30)
    # Wait for logo
    wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Logo']")))

    # Login
    driver.find_element(By.ID, "emailInput").send_keys("bankdata2@gmail.com")
    driver.find_element(By.ID, "passwordInput").send_keys("Admin@123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait until loader disappears and dashboard is visible
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.loaderContainer")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='widget-title']")))

    yield driver
    time.sleep(2)
    driver.quit()


def wait_for_clickable(driver, locator, timeout=30):
    """
    Wait for an element to be clickable and click it.
    Handles intercepted clicks by falling back to JS click.
    """
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.element_to_be_clickable(locator))
    try:
        element.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", element)
    return element


def wait_for_visibility(driver, locator, timeout=30):
    """Wait for element visibility"""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located(locator))


# -------------------- TESTS --------------------

def test_home_page_login_verification(setup_and_teardown):

    assert driver.find_element(By.XPATH, "//span[contains(text(),'Merchant ID:')]").is_displayed()


def test_home_page_top_navbar_merchant_view_option_verification(setup_and_teardown):
    # Wait until loader disappears
    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.loaderContainer"))
    )

    dropdown = wait_for_clickable(driver, (By.XPATH, "//div[@class='selectField__input-container css-19bb58m']"))
    dropdown.click()

    # Select first dropdown option explicitly
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'selectField__option')]"))
    )
    option.click()

    # Wait for dashboard to render
    my_accounts_header = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//h4[@class='myAccountsHeader']"))
    )
    assert my_accounts_header.is_displayed()

    # Close account view
    driver.find_element(By.XPATH, "//div[@class='icon-container']//*[name()='svg']").click()
    WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.loaderContainer")))
    assert driver.find_element(By.XPATH, "//div[@class='widget-title']").is_displayed()



def test_home_page_top_navbar_search_invalid_transaction_ID_functionality(setup_and_teardown):

    transaction_field = driver.find_element(By.XPATH, "//input[@placeholder='Transaction ID']")
    transaction_field.send_keys("123456")

    # Use Enter instead of clicking search icon
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    wait_for_visibility(driver, (By.XPATH, "//div[@class='id-notfound']"))
    assert driver.find_element(By.XPATH, "//div[@class='id-notfound']").is_displayed()


def test_home_page_top_navbar_support_functionality(setup_and_teardown):


    # Click support button safely
    wait_for_clickable(driver, (By.ID, "support"))

    # Wait for Service Tickets option and click
    wait_for_clickable(driver, (By.XPATH, "//p[@class='popover-texts'][normalize-space()='Service Tickets']"))
