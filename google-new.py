from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com/")
    time.sleep(3)
    actualTitle = driver.title
    if actualTitle == "Google":
        searchBox = driver.find_element(By.XPATH,"//*[@id='APjFqb']")
        searchBox.send_keys("Iphone 16")
        searchBox.send_keys(Keys.RETURN)
        time.sleep(4)
        print("Test Pass")

    else:
        print("Test Fail")

finally:
    driver.quit()