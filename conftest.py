import os
from datetime import datetime

import pytest

from utils.driver_factory import get_driver

ARTIFACT_DIR = "artifacts"


@pytest.fixture
def driver():
    """Provide a fresh WebDriver per test and always quit it afterwards."""
    drv = get_driver()
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save a screenshot when a test fails, for CI artifact upload."""
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    drv = item.funcargs.get("driver")
    if drv is None:
        return

    os.makedirs(ARTIFACT_DIR, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(ARTIFACT_DIR, f"{item.name}_{stamp}.png")
    try:
        drv.save_screenshot(path)
        print(f"\nSaved failure screenshot: {path}")
    except Exception as exc:  # screenshot is best-effort
        print(f"\nCould not save screenshot: {exc}")
