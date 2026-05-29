import requests
from selenium.webdriver.common.by import By
from  selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.onlinekhabar.com/")
driver.maximize_window()
time.sleep(5)
links = driver.find_elements(By.XPATH, "//a")
print(f"Total elements found: ", len(links))
time.sleep(5)

for link in links:
     url = link.get_attribute("href")

     response = requests.head(
         url
     )
     if response.status_code >= 400:
         print("Broken link")
     else:
         print("Valid link")

time.sleep(5)
driver.quit()