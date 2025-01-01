from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com/")
    driver.maximize_window()
    time.sleep(3)
    actualTitle = driver.title
    if actualTitle == "Google":
        #copy paste xpath"
        #searchBox = driver.find_element(By.XPATH,"//*[@id='APjFqb']")
        #copy paste full xpath
        searchBox = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea")
        searchBox.send_keys("Iphone 16")
        searchBox.send_keys(Keys.ENTER)
        
        WebDriverWait(driver,40).until(expected_conditions.presence_of_element_located((By.ID,"search")))
        searchResult = driver.find_elements(By.XPATH,"//h3[contains(@class,'LC20lb MBeuO DKV0Md')]")
        print(len(searchResult))
        
        for i in range(0,len(searchResult)):
            print(searchResult[i].text)

    else:
        print("Test Fail")

finally:
    driver.quit()