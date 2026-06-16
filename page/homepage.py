from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class HomePage:

    HOME_LINK = (By.XPATH, "//a[@href='https://souvenir.edu.np']")
    ABOUT_LINK = (By.XPATH, "//a[@href='https://souvenir.edu.np/about']")
    GALLERY_LINK = (By.XPATH, "//a[@href='https://souvenir.edu.np/galleryMain']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_nav(self, locator, name):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        time.sleep(2)
        print(f"Navigated to: {name} | URL: {self.driver.current_url}")

    def go_home(self):
        self.driver.get("https://souvenir.edu.np/")
        time.sleep(2)

    def click_home(self):
        self.click_nav(self.HOME_LINK, "Home")

    def click_about(self):
        self.click_nav(self.ABOUT_LINK, "About Us")

    def click_gallery(self):
        self.click_nav(self.GALLERY_LINK, "Gallery")

  
   

    def navigate_all(self):

        print("\nStarting full navigation test...\n")

        print("Step 1: Clicking HOME")
        self.click_home()
        self.go_home()

        print("Step 2: Clicking ABOUT US")
        self.click_about()
        self.go_home()

        print("Step 3: Clicking GALLERY")
        self.click_gallery()
        self.go_home()



        print("\nAll navigation links tested successfully!\n")