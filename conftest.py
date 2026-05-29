import pytest
from selenium import webdriver
import pytest_html

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":

        extras.append(pytest_html.extras.url("http://www.example.com/"))
        extras.append(pytest_html.extras.text("some string", name="Different title"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):

            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extras


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed during the 'call' phase
    if report.when == 'call' and report.failed:
        # Retrieve the driver fixture from the test item
        driver = item.funcargs.get('setup_driver')
        if driver:
            report_name = item.nodeid.replace("::", "_").replace(".py", "")
            driver.save_screenshot(f"screenshots/{report_name}.png")

def _capture_screenshot(driver, path):
    driver.get_screenshot_as_png()