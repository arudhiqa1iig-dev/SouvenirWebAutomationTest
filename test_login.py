import sys
import time
from utils.driver_factory import get_driver
from page.login_page import LoginPage
from page.homepage import HomePage
from page.carousel_page import CarouselPage
from page.contact_page import ContactPage

driver = get_driver()
failed = False

try:
    print("1. Opening Souvenir website")
    driver.get("https://souvenir.edu.np/")
    time.sleep(3)

    assert driver.title.strip() != "", "Homepage title is empty - site may be down"
    print(f"   Homepage loaded. Title: {driver.title}")

    print("2. Testing all navigation links")
    home = HomePage(driver)
    home.navigate_all()

    print("3. Back on homepage - testing carousel arrows")
    driver.get("https://souvenir.edu.np/")
    time.sleep(3)
    carousel = CarouselPage(driver)
    carousel.click_through_slides(total_slides=11, carousel_index=0, pause=1.0)

    print("4. Opening Contact Us page")
    driver.get("https://souvenir.edu.np/contact")
    time.sleep(10)
    
    contact = ContactPage(driver)
    contact.fill_contact_form(
        name="Test User",
        email="testuser@example.com",
        subject="Automation Test Inquiry",
        message="This is an automated test message sent via Selenium."
    )

    print("5. Login page opened")
    driver.get("https://school.techarttrekkies.com/school-login")
    login = LoginPage(driver)

    print("6. Entering credentials")
    login.login("wronguser", "wrongpass")
    time.sleep(5)

    print("7. Login attempted")
    assert "login" in driver.current_url.lower(), \
        "Wrong credentials should NOT log in, but page left the login screen"
    print(f"   Still on login page as expected: {driver.current_url}")

    print("All checks completed successfully")

except Exception as e:
    print("ERROR OCCURRED ")
    print(e)
    failed = True

finally:
    print("Closing browser")
    driver.quit()

if failed:
    sys.exit(1)
