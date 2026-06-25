from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AboutPage:

    URL = "https://souvenir.edu.np/about"

    HEADING = (By.TAG_NAME, "h1")
    BODY = (By.TAG_NAME, "body")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.presence_of_element_located(self.BODY))
        print(f"Opened About page | URL: {self.driver.current_url}")

    def get_heading_text(self):
        try:
            heading = self.wait.until(
                EC.visibility_of_element_located(self.HEADING)
            )
            return heading.text.strip()
        except Exception as e:
            print(f"ERROR reading heading: {e}")
            return ""

    def get_body_text(self):
        body = self.wait.until(EC.presence_of_element_located(self.BODY))
        return body.text.strip()
