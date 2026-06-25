import os

from selenium import webdriver


def get_driver():
    """Create a Chrome WebDriver.

    Runs headless by default. Set HEADLESS=false to watch the browser
    locally (useful when debugging a failing test).
    """
    options = webdriver.ChromeOptions()

    headless = os.getenv("HEADLESS", "true").lower() != "false"
    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # Identify the suite in server logs so the site owner can recognise
    # (and, if ever needed, block) this automated traffic.
    options.add_argument(
        "--user-agent=SouvenirWebAutomationTest/1.0 (Selenium monitoring bot)"
    )

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)
    return driver
