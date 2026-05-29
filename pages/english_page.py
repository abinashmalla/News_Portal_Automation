import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EnglishPage(BasePage):

    POLITICS = (By.XPATH, "//li[@id='menu-item-454648']//a[normalize-space()='Politics']")
    ECONOMY = (By.XPATH, "//li[@id='menu-item-454649']//a[normalize-space()='Economy']")
    SEARCH_ICON = (By.CSS_SELECTOR, "span")
    SEARCH_BOX = (By.XPATH, "//div[@class='ok-top-right']//i[@class='ok-search-icon']")
    search_location = (By.XPATH, "//input[@placeholder='Search …']")
    SEARCH_BTN = (By.XPATH, "//input[@value='Search']")
    TECHNOLOGY = (By.LINK_TEXT, "Technology")
    NEXT_BTN = (By.LINK_TEXT, "Next")
    NEPALI = (By.LINK_TEXT, "नेपाली")

    def open_search(self):
         self.click(*self.SEARCH_BOX)
         time.sleep(4)
         self.click(*self.search_location).clear().send_keys("Todays News")
         time.sleep(4)
         self.click(*self.SEARCH_BTN)

    def open_politics(self):
         self.click(self.POLITICS)

    def open_economy(self):
         self.click(self.ECONOMY)

    def open_technology(self):
        self.click(self.TECHNOLOGY)

    def next_page(self):
        self.click(self.NEXT_BTN)

    def open_nepali(self):
        self.click(self.NEPALI)

    def execute_script(self, param):
        pass

