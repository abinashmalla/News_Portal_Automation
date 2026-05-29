import time
import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver

@pytest.mark.parametrize("browser", ["chrome"])
def test_login(browser):
    driver = get_driver("chrome")
    driver.get("https://www.onlinekhabar.com/")
    driver.maximize_window()
    time.sleep(5)
    search_box=driver.find_element(By.CSS_SELECTOR,"div[class='ok-container flx'] input[placeholder='Search Keywords']")
    time.sleep(3)
    search_box.send_keys("Today News")
    time.sleep(3)
    search_button=driver.find_element(By.XPATH,"//div[@class='ok-container flx']//img[@alt='Search']")
    search_button.click()
    time.sleep(4)

def test_search():
    driver = get_driver("chrome")
    driver.get("https://english.onlinekhabar.com/?s=business")
    driver.maximize_window()
    time.sleep(3)
    search_box=driver.find_element(By.XPATH,"//div[@class='ok-top-right']//span[@class='ok-search-btn']")
    search_box.click()
    time.sleep(3)
    search_location=driver.find_element(By.XPATH,"//input[@placeholder='Search …']")
    search_location.click()
    search_location.clear()
    time.sleep(3)
    search_location.send_keys("Today News")
    time.sleep(3)
    search_button=driver.find_element(By.XPATH,"//input[@value='Search']")
    search_button.click()
    time.sleep(5)