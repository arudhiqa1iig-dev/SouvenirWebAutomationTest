"""Homepage smoke + navigation + carousel checks."""
import config
from page.homepage import HomePage
from page.carousel_page import CarouselPage


def test_homepage_loads(driver):
    driver.get(config.BASE_URL)
    assert driver.title.strip() != "", "Homepage title is empty - site may be down"


def test_navigation_links(driver):
    driver.get(config.BASE_URL)
    home = HomePage(driver)
    home.navigate_all()


def test_carousel_steps_through_slides(driver):
    driver.get(config.BASE_URL)
    carousel = CarouselPage(driver)
    carousel.click_through_slides(total_slides=11, carousel_index=0, pause=1.0)
