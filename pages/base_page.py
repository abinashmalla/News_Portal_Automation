from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, by_locator):
        try:
            self.wait.until(
                EC.element_to_be_clickable(by_locator)
            ).click()
        except TimeoutException:
            self.take_screenshot("click_timeout")
            raise Exception(f"Timeout while clicking: {by_locator}")

    def send_keys(self, by_locator, text):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(by_locator)
            )
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            self.take_screenshot("sendkeys_timeout")
            raise Exception(f"Timeout while entering text: {by_locator}")

    def get_element(self, by_locator):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(by_locator)
            )
        except TimeoutException:
            self.take_screenshot("element_timeout")
            raise Exception(f"Element not found: {by_locator}")

    def open(self, url):
        self.driver.get(url)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def take_screenshot(self, param):
        pass