from selenium import webdriver
import time
from pages.login_page import LoginPage
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize( "username,password",[
    ("abinashmalla","Omabinash100"),
    ("omabinash","omabinash500")

])
def test_login_page(driver,username,password):
    login_page = LoginPage(driver)
    login_page.open_url("https://www.onlinekhabar.com/login?redirect_url=https%3A%2F%2Fwww.onlinekhabar.com%2Fmarkets%2F")
    driver.maximize_window()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    time.sleep(3)

    try:
        if "markets" in driver.page_source:
            print("Login Successfull")
            assert True
        else:
            raise AssertionError("Login Failed")
    except Exception as e:
        print(f"Error: {str(e)}")
        assert False