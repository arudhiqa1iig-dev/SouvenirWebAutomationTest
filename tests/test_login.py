"""School portal login page check.

Read-only: verifies the login form renders. It does NOT submit
credentials, so it never performs an auth attempt against the live
portal (avoids lockouts / rate limits from a twice-daily schedule).
"""
import config
from page.login_page import LoginPage


def test_login_form_renders(driver):
    driver.get(config.SCHOOL_LOGIN_URL)
    login = LoginPage(driver)
    assert login.fields_present(), "Login form fields did not render"
