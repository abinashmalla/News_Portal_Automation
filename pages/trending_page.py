import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Trending_Page(BasePage):

    arrow_box = (By.XPATH,"//div[@class='ok-icon-trending trending-trigger']//*[name()='svg']")
    close_arrow = (By.XPATH,"//h2[contains(text(),'ट्रेन्डिङ')]//span[@class='close-drawer'][normalize-space()='+']")

    def open_Trending(self):
         self.click(self.arrow_box)
         time.sleep(2)
         self.click(self.close_arrow)
