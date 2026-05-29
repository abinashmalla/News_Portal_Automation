from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MarketPage(BasePage):

    TOOLS = (By.XPATH, "//header//*[contains(text(),'Tools')]")
    MENU = (By.CSS_SELECTOR, ".primary-menu-trigger")
    HOMEPAGE = (By.XPATH, "//li[contains(.,'होमपेज')]")
    PATRO = (By.LINK_TEXT, "पात्रो")

    def click_tools(self):
        self.click(self.TOOLS)

    def open_menu(self):
        self.click(self.MENU)

    def click_homepage(self):
        self.click(self.HOMEPAGE)

    def open_patro(self):
        self.click(self.PATRO)