import time
import pytest
from utils.driver_factory import get_driver
from pages.home_page import HomePage

@pytest.mark.parametrize("browser", ["chrome"])
def test_links(browser,driver):
     driver = get_driver("chrome")
     homepage = HomePage(driver)
     driver.get("https://www.onlinekhabar.com/")
     time.sleep(5)
     driver.maximize_window()
     time.sleep(3)
     homepage.test_homepage_title(driver)
     time.sleep(3)
     driver.quit()