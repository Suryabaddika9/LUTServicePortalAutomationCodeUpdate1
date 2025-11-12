import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from utilities.wait_helpers import wait_for_element

def scroll_and_click_button(driver, by_type, locator, timeout=20):
    """
    Scrolls to a button and clicks it safely with fallback handling.

    :param driver: WebDriver instance
    :param by_type: selenium.webdriver.common.by.By (e.g., By.ID, By.CSS_SELECTOR)
    :param locator: Locator string
    :param timeout: Timeout for waiting (default 20 seconds)
    """
    try:
        # Wait for the button to be visible
        button = wait_for_element(driver, by_type, locator, timeout=timeout, condition="clickable")

        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(1)  # Optional wait for animations

        # Try clicking
        button.click()

    except ElementClickInterceptedException:
        print("Click intercepted. Trying JavaScript click.")
        driver.execute_script("arguments[0].click();", button)

    except TimeoutException:
        print(f"Button not found or not clickable: {locator}")
        driver.save_screenshot("button_click_error.png")
        raise