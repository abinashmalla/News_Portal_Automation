import time
import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver


@pytest.mark.parametrize("browser", ["chrome"])
def test_footer(browser):
    driver = get_driver("chrome")
    driver.get("https://www.onlinekhabar.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    x = 0
    while True:
          x += 1
          driver.execute_script("scrollBy(0,300)")
          time.sleep(0.5)
          if x > 100:
              break
    element = driver.find_element(By.XPATH, "//a[contains(text(),'समाज')]")
    element.click()
    time.sleep(5)


    while True:
          x += 1
          driver.execute_script("scrollBy(0,300)")
          time.sleep(0.5)
          if x > 100:
              break
    element1= driver.find_elements(By.XPATH,"//img[@alt='Download for IOS']")
    element1[0].click()
    time.sleep(5)

