from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.youtube.com/")
    time.sleep(3)
    search = driver.find_element(By.NAME, "search_query")
    search.send_keys("Ncs")
    time.sleep(3)
    search.send_keys(Keys.RETURN)
    time.sleep(3)

finally:
    driver.quit()