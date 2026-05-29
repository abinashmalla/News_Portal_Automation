from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


def test_homepage_title(driver):
    driver.get("https://www.onlinekhabar.com")
    assert "Online Khabar" in driver.title


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.popup = (By.XPATH,"//span[@class='ok_roadblok_skip']")
        self.news_box = (By.XPATH, "//a[@href='https://www.onlinekhabar.com/content/news/rastiya']")
        self.lifestyle_box = (By.XPATH, "//a[@href='https://www.onlinekhabar.com/lifestyle']")
        self.other = (By.XPATH, "//a[@href='#'][contains(text(),'अन्य')]")
        self.select_box = (By.XPATH, "//div[@class='ok-user-activity']//span[@class='ok-push-menu-trigger']")
        self.english_box=(By.XPATH,"//span[normalize-space()='English']")
        self.search_box = (By.CSS_SELECTOR, "div[class='ok-container flx'] input[placeholder='Search Keywords']")
        self.search_button = (By.XPATH, "//div[@class='ok-container flx']//img[@alt='Search']")
        # self.POLITICS = (By.XPATH, "//li[@id='menu-item-454648']//a[normalize-space()='Politics']")
        # self.ECONOMY = (By.XPATH, "//li[@id='menu-item-454649']//a[normalize-space()='Economy']")


    def take_screenshot(self, name):
        # Saves the screenshot to a specific folder
        self.driver.save_screenshot(f"./screenshots/{name}.png")

    def test_homepage_title(self,driver):
        self.driver.get("https://www.onlinekhabar.com")
        assert "Online Khabar" in driver.title


    def open_ads_page(self):
        try:
           self.driver.find_element(*self.popup).click()
        except:
            print("No popup found")

    def open_popup(self):
        self.driver.find_element(*self.popup).click()

    def open_page(self):
        self.driver.get("https://www.onlinekhabar.com/")

    def open_news_page(self):
        self.driver.find_element(*self.news_box).click()

    def open_Hover_effect(self):
         self.driver.find_element(*self.lifestyle_box).click()

    def open_other(self):
        self.driver.find_element(*self.other).click()

    def open_search_box(self):
          self.driver.find_element(*self.search_box).send_Keys("Today News").send_keys(Keys.RETURN)
          time.sleep(3)

    def open_select_box(self):
         self.driver.find_element(*self.select_box).click()

    def open_english(self):
        self.driver.find_element(*self.english_box).click()



