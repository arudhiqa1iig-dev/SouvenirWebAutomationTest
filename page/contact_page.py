from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

class ContactPage:
   
    FORM = (By.ID, "contactForm")
    NAME_FIELD = (By.CSS_SELECTOR, "#contactForm input[name='name']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#contactForm input[name='email']")
    MESSAGE_FIELD = (By.CSS_SELECTOR, "#contactForm textarea[name='message']")
    SUBJECT_FIELD = (By.CSS_SELECTOR, "#contactForm input[name='subject']")
      


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # def _find_first(self, candidates, field_name):
    #     for locator in candidates:
    #         try:
    #             element = self.wait.until(EC.presence_of_element_located(locator))
    #             if element.is_displayed():
    #                 print(f"  -> {field_name} matched locator: {locator}")
    #                 return element
    #         except Exception:
    #             continue
    #     raise NoSuchElementException(f"Could not locate field: {field_name}")

    
    def _safe_type(self, locator, field_name, value):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(value)
            print(f"Filled: {field_name} = {value}")
        except Exception as e:
            print(f"ERROR filling {field_name}: {e}")


    def scroll_to_form(self):
        try:
            form = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", form
            )
            time.sleep(1)
            print("Scrolled down to the contact form")
        except Exception as e:
            print(f"ERROR scrolling to contact form: {e}")

    def fill_contact_form(self, name, email, subject, message):
        print("\nFilling contact form...\n")
        self.scroll_to_form()
        self._safe_type(self.NAME_FIELD, "Name", name)
        self._safe_type(self.EMAIL_FIELD, "Email", email)
        self._safe_type(self.SUBJECT_FIELD, "Subject", subject)
        self._safe_type(self.MESSAGE_FIELD, "Message", message)

   