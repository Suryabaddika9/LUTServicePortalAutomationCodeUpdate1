import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.wait_helpers import wait_for_element

def get_otp_key():
    """
    Generates OTP by automating the TOTP generator website using Selenium.
    Returns the OTP as a string.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://totp.danhersam.com/")

        wait_for_element(driver, By.CSS_SELECTOR, "h1.title", timeout=10, condition="visible")

        secret_key = driver.find_element(By.CSS_SELECTOR, "input[placeholder='The secret key (in base-32 format)']")
        secret_key.clear()
        secret_key.send_keys("GUYTONJZGYYTSNRS")

        time_out = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Usually 30']")
        time_out.clear()
        time_out.send_keys("60")

        time.sleep(2)  # Wait for OTP to generate

        otp = driver.find_element(By.ID, "token").text
        return otp

    finally:
        driver.quit()  # Ensures browser is closed even if an error occurs





































