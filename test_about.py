import sys
import time
from utils.driver_factory import get_driver
from page.about_page import AboutPage

driver = get_driver()
failed = False

try:
    print("1. Opening About page")
    about = AboutPage(driver)
    about.open()
    time.sleep(2)

    print("2. Checking page title")
    assert driver.title.strip() != "", "About page title is empty - site may be down"
    print(f"   Title: {driver.title}")

    print("3. Checking URL stayed on About")
    assert "about" in driver.current_url.lower(), \
        f"Expected About URL, got {driver.current_url}"

    print("4. Checking page has visible content")
    body_text = about.get_body_text()
    assert len(body_text) > 50, "About page has little or no text - page may be broken"
    print(f"   Body text length: {len(body_text)} chars")

    print("5. Checking heading is present")
    heading = about.get_heading_text()
    print(f"   Heading: {heading!r}")

    print("All About page checks completed successfully")

except Exception as e:
    print("ERROR OCCURRED ")
    print(e)
    failed = True

finally:
    print("Closing browser")
    driver.quit()

if failed:
    sys.exit(1)
