import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wait_for_element(driver, locator_type, locator_value, timeout=20, condition="visible", retries=3, retry_delay=2):
    """
    Reusable method to wait for an element with flexible conditions and retry support.

    :param driver: WebDriver instance
    :param locator_type: selenium.webdriver.common.by.By (e.g., By.XPATH, By.ID)
    :param locator_value: The locator string (e.g., "//button[@id='login']")
    :param timeout: Maximum time to wait in seconds (default 20)
    :param condition: Condition type - "visible", "clickable", "present", or "invisible"
    :param retries: Number of retry attempts (default 3)
    :param retry_delay: Delay between retries in seconds (default 2)
    :return: The WebElement (except for 'invisible', which returns True/False)
    """
    attempt = 0
    while attempt < retries:
        try:
            wait = WebDriverWait(driver, timeout)
            if condition == "visible":
                return wait.until(EC.visibility_of_element_located((locator_type, locator_value)))
            elif condition == "clickable":
                return wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
            elif condition == "present":
                return wait.until(EC.presence_of_element_located((locator_type, locator_value)))
            elif condition == "invisible":
                return wait.until(EC.invisibility_of_element_located((locator_type, locator_value)))
            else:
                raise ValueError(f"Unsupported condition type: {condition}")
        except TimeoutException:
            attempt += 1
            if attempt < retries:
                time.sleep(retry_delay)
            else:
                raise TimeoutException(f"Element not found: {locator_type}='{locator_value}' after {timeout}s and {retries} retries")

def wait_for_elements(driver, locator_type, locator_value, timeout=20, condition="visible", retries=3, retry_delay=2):
    """
    Reusable method to wait for an element with flexible conditions and retry support.

    :param driver: WebDriver instance
    :param locator_type: selenium.webdriver.common.by.By (e.g., By.XPATH, By.ID)
    :param locator_value: The locator string (e.g., "//button[@id='login']")
    :param timeout: Maximum time to wait in seconds (default 20)
    :param condition: Condition type - "visible", "clickable", "present", or "invisible"
    :param retries: Number of retry attempts (default 3)
    :param retry_delay: Delay between retries in seconds (default 2)
    :return: The WebElement (except for 'invisible', which returns True/False)
    """
    attempt = 0
    while attempt < retries:
        try:
            wait = WebDriverWait(driver, timeout)
            if condition == "visible":
                return wait.until(EC.visibility_of_element_located((locator_type, locator_value)))
            elif condition == "clickable":
                return wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
            elif condition == "present":
                return wait.until(EC.presence_of_element_located((locator_type, locator_value)))
            elif condition == "invisible":
                return wait.until(EC.invisibility_of_element_located((locator_type, locator_value)))
            else:
                raise ValueError(f"Unsupported condition type: {condition}")
        except TimeoutException:
            attempt += 1
            if attempt < retries:
                time.sleep(retry_delay)
            else:
                raise TimeoutException(f"Element not found: {locator_type}='{locator_value}' after {timeout}s and {retries} retries")
