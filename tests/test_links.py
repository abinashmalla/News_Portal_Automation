import time
import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver


@pytest.mark.parametrize("browser", ["chrome"])
def test_links(browser):
    driver = get_driver("chrome")
    driver.get("https://www.onlinekhabar.com/")
    driver.maximize_window()
    time.sleep(3)

    link = driver.find_element(By.LINK_TEXT, "सम्पर्क")
    driver.execute_script("arguments[0].scrollIntoView(true);", link)
    time.sleep(3)
    link.click()

    time.sleep(5)
    driver.quit()

