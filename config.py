"""Central configuration for the Selenium test suite.

Values can be overridden via environment variables so the same tests
run locally and in CI without code changes.
"""
import os

BASE_URL = os.getenv("BASE_URL", "https://souvenir.edu.np")
SCHOOL_LOGIN_URL = os.getenv(
    "SCHOOL_LOGIN_URL", "https://school.techarttrekkies.com/school-login"
)

# Default explicit-wait timeout (seconds) used across page objects.
DEFAULT_TIMEOUT = int(os.getenv("SELENIUM_TIMEOUT", "15"))
