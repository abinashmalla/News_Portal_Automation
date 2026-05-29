import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
import time

@pytest.mark.parametrize( "username,password",[
    ("abinashmalla","Omabinash100"),
    ("omabinash","omabinash500")

])

@pytest.mark.parametrize("browser", ["chrome", "firefox","ChromiumEdge"])
def test_login(browser, username, password):
    driver = get_driver(browser)
    login_page = LoginPage(driver)
    driver.get("https://www.onlinekhabar.com/login?redirect_url=https%3A%2F%2Fwww.onlinekhabar.com%2Fmarkets%2F")
    driver.maximize_window()
    time.sleep(2)
    login_page.enter_username(username)
    time.sleep(2)
    login_page.enter_password(password)
    login_page.click_login()
    time.sleep(2)
    driver.quit()