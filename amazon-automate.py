from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.amazon.in/")
    time.sleep(3)
    searchTextBox = driver.find_element(By.ID, "twotabsearchtextbox")
    searchTextBox.send_keys("Iphone 16")
    searchTextBox.send_keys(Keys.RETURN)
    time.sleep(5)
    print("Pass")

finally:
    driver.quit()