import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CarouselPage:
    
    PREV_ARROWS = (By.CSS_SELECTOR, ".owl-prev")
    NEXT_ARROWS = (By.CSS_SELECTOR, ".owl-next")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

 
    def _click_element(self, element, label):
        try:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", element
            )
            time.sleep(0.3)
            try:
                element.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", element)
            print(f"Clicked: {label}")
            return True
        except Exception as e:
            print(f"ERROR clicking {label}: {e}")
            return False

    def _click_all(self, locator, label_prefix, clicks_per_arrow, pause):
        arrows = self.driver.find_elements(*locator)
        print(f"Found {len(arrows)} {label_prefix} arrow(s)")

        for index in range(len(arrows)):
            # Re-find on every iteration in case the carousel re-renders
            # the DOM after a click (owl-carousel often does this).
            arrows = self.driver.find_elements(*locator)
            if index >= len(arrows):
                break
            for _ in range(clicks_per_arrow):
                self._click_element(arrows[index], f"{label_prefix} #{index + 1}")
                time.sleep(pause)

    def click_all_prev_arrows(self, clicks_per_arrow=1, pause=0.5):
        self._click_all(self.PREV_ARROWS, "owl-prev", clicks_per_arrow, pause)

    def click_all_next_arrows(self, clicks_per_arrow=1, pause=0.5):
        self._click_all(self.NEXT_ARROWS, "owl-next", clicks_per_arrow, pause)

    def cycle_all_carousels(self, clicks_per_arrow=2, pause=0.5):
        print("\nStarting carousel navigation test...\n")
        self.click_all_next_arrows(clicks_per_arrow=clicks_per_arrow, pause=pause)
        self.click_all_prev_arrows(clicks_per_arrow=clicks_per_arrow, pause=pause)
        print("\nCarousel navigation test completed.\n")

    def click_through_slides(self, total_slides, carousel_index=0, pause=1.0):
        arrows = self.driver.find_elements(*self.NEXT_ARROWS)
        print(f"Found {len(arrows)} owl-next arrow(s) on the page")

        if not arrows or carousel_index >= len(arrows):
            print(f"ERROR: owl-next arrow at index {carousel_index} not found")
            return


        for slide_number in range(2, total_slides + 1):
            arrows = self.driver.find_elements(*self.NEXT_ARROWS)
            if carousel_index >= len(arrows):
                print(f"ERROR: lost reference to owl-next arrow at slide {slide_number}")
                break
            self._click_element(arrows[carousel_index], f"owl-next -> slide {slide_number}")
            time.sleep(pause)

        
