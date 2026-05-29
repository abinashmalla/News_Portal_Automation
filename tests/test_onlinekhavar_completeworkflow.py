from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pages.english_page import EnglishPage
from pages.home_page import HomePage
from pages.search_text import Search_Page
from pages.trending_page import Trending_Page
import pytest
from pages.market_page import MarketPage
from selenium.common.exceptions import NoAlertPresentException
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    try:
         close_ad = driver.find_element(By.CLASS_NAME, "close-ad")
         close_ad.click()
    except:
         print("No popup found")

    driver.maximize_window()
    yield driver
    driver.quit()

def test_workflow(driver):
    home_page = HomePage(driver)

    try:
        alert = driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        print('No alert is present.')

    english_page = EnglishPage(driver)
    trending_page = Trending_Page(driver)
    market_page = MarketPage(driver)
    login_page = LoginPage(driver)
    search_box = Search_Page(driver)
    home_page.open_page()

    time.sleep(3)
    driver.maximize_window()
    time.sleep(2)
    login_page.open_url("https://www.onlinekhabar.com/login?redirect_url=https%3A%2F%2Fwww.onlinekhabar.com%2Fmarkets%2F")
    time.sleep(3)
    login_page.enter_username("abinashmalla")
    time.sleep(3)
    login_page.enter_password("password")
    time.sleep(3)
    login_page.click_login()
    time.sleep(3)
    home_page.open_news_page()
    time.sleep(3)

    search_box.open_search()
    time.sleep(3)

    home_page.open_Hover_effect()
    time.sleep(3)

    home_page.open_other()
    time.sleep(2)

    home_page.open_select_box()
    time.sleep(3)

    home_page.open_english()
    time.sleep(4)

    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(5)

    english_page.open_politics()
    time.sleep(3)

    english_page.open_economy()
    time.sleep(5)

    english_page. open_technology()
    time.sleep(3)


    english_page.next_page()
    time.sleep(5)

    english_page.open_nepali()

    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(3)

    trending_page.open_Trending()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(3)
    market_page.open_patro()
    time.sleep(5)

