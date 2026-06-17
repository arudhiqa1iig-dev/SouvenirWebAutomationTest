from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:

    # Main navigation
    HOME_LINK = (By.XPATH, "//a[@href='https://souvenir.edu.np']")
    ABOUT_LINK = (By.XPATH, "//a[@href='https://souvenir.edu.np/about']")
    GALLERY_LINK = (By.XPATH, "//a[@href='https://souvenir.edu.np/galleryMain']")

    # Dropdown items under About Us
    OVERVIEW_LINK = (By.XPATH, "//a[normalize-space()='Overview']")
    GET_IN_TOUCH_LINK = (By.XPATH, "//a[contains(normalize-space(),'Get')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

   
    # CORE SAFE CLICK METHOD
   
    def safe_click(self, locator, name):
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            print(f"Clicked: {name} | URL: {self.driver.current_url}")
        except Exception as e:
            print(f"ERROR clicking {name}: {e}")

   
    # NAVIGATION METHODS

    def click_home(self):
        self.safe_click(self.HOME_LINK, "Home")

    def click_about(self):
        self.safe_click(self.ABOUT_LINK, "About Us")

    def click_gallery(self):
        self.safe_click(self.GALLERY_LINK, "Gallery")

   
    # DROPDOWN HANDLING
    
    def open_about_dropdown(self):
        try:
            about = self.wait.until(
                EC.visibility_of_element_located(self.ABOUT_LINK)
            )
            self.actions.move_to_element(about).perform()
            print("Hovered on About Us")
        except Exception as e:
            print(f"ERROR hovering About Us: {e}")

    def click_overview(self):
        try:
            self.open_about_dropdown()

            overview = self.wait.until(
                EC.visibility_of_element_located(self.OVERVIEW_LINK)
            )
            overview.click()
            print("Clicked: Overview")

        except Exception as e:
            print(f"ERROR clicking Overview: {e}")

    def click_get_in_touch(self):
        try:
            self.open_about_dropdown()

            get_in_touch = self.wait.until(
                EC.visibility_of_element_located(self.GET_IN_TOUCH_LINK)
            )
            get_in_touch.click()
            print("Clicked: Get In Touch")

        except Exception as e:
            print(f"ERROR clicking Get In Touch: {e}")

   
    # FULL TEST FLOW
   
    def navigate_all(self):

        print("\nStarting navigation test...\n")

        self.click_home()
        self.click_about()
        self.click_gallery()
        self.click_overview()
        self.click_get_in_touch()

        print("\nNavigation test completed.\n")