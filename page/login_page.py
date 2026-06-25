from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config


class LoginPage:

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SIGN_IN_BTN = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)

    def fields_present(self):
        """Return True if all login form fields render. No submit, so this
        is safe to run against the live portal without an auth attempt."""
        for locator in (self.USERNAME, self.PASSWORD, self.SIGN_IN_BTN):
            self.wait.until(EC.presence_of_element_located(locator))
        return True

    def login(self, username, password):
        """Fill and submit the login form. Performs a real auth attempt -
        not used by the scheduled suite to avoid hitting the portal."""
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SIGN_IN_BTN).click()
