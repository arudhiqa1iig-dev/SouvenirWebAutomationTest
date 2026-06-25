"""Contact form fill check."""
import config
from page.contact_page import ContactPage


def test_contact_form_can_be_filled(driver):
    driver.get(f"{config.BASE_URL}/contact")
    contact = ContactPage(driver)
    contact.fill_contact_form(
        name="Test User",
        email="testuser@example.com",
        subject="Automation Test Inquiry",
        message="This is an automated test message sent via Selenium.",
    )
