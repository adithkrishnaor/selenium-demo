from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com/")
    searchTextBox = driver.find_element(By.ID,"APjFqb")
    searchTextBox.send_keys("Fisat")
    searchTextBox.send_keys(Keys.RETURN)
    time.sleep(5)

finally:
    driver.quit()