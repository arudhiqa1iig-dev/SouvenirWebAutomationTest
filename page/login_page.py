from selenium.webdriver.common.by import By

class LoginPage:

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SIGN_IN_BTN = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SIGN_IN_BTN).click()