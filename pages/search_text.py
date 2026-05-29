import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class Search_Page(BasePage):

    search_box = (By.CSS_SELECTOR,"div[class='ok-container flx'] input[placeholder='Search Keywords']")
    search_button = (By.XPATH,"//div[@class='ok-container flx']//img[@alt='Search']")
    search = (By.NAME,"s")
    def open_search(self):
        self.driver.find_element(*self.search_box).send_keys("Today hot news")
        time.sleep(2)
        self.driver.find_element(*self.search_button).click()
        time.sleep(3)




