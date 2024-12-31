from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://fisat.ac.in/")
    findAcad = driver.find_element(By.ID,"menu-item-4054")
    time.sleep(2)
    findAcad.click()
    
    findDep = driver.find_element(By.ID,"menu-item-dropdown-4059")
    time.sleep(2)
    findDep.click()

    findMca = driver.find_element(By.ID,"menu-item-dropdown-4144")
    time.sleep(2)
    findMca.click()

    time.sleep(5)
    
finally:
    driver.quit()