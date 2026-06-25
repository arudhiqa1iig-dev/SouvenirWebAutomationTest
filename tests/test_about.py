"""About page content checks."""
from page.about_page import AboutPage


def test_about_page_loads(driver):
    about = AboutPage(driver)
    about.open()
    assert driver.title.strip() != "", "About page title is empty - site may be down"


def test_about_url_is_correct(driver):
    about = AboutPage(driver)
    about.open()
    assert "about" in driver.current_url.lower(), \
        f"Expected About URL, got {driver.current_url}"


def test_about_has_content(driver):
    about = AboutPage(driver)
    about.open()
    body_text = about.get_body_text()
    assert len(body_text) > 50, "About page has little or no text - page may be broken"
