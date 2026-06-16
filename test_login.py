import time
from utils.driver_factory import get_driver
from page.login_page import LoginPage
from page.homepage import HomePage

driver = get_driver()

try:
    print("1. Opening Souvenir website")
    driver.get("https://souvenir.edu.np/")
    time.sleep(3)

    print("2. Testing all navigation links")
    home= HomePage(driver)
    home.navigate_all()

    print("3. Login page opened")
    driver.get("https://school.techarttrekkies.com/school-login")
    login = LoginPage(driver)

    print("4. Entering credentials")
    login.login("wronguser", "wrongpass")
    time.sleep(5)

    print("5. Login attempted")

except Exception as e:
    print("ERROR OCCURRED ")
    print(e)

finally:
    print("Closing browser")
    driver.quit()