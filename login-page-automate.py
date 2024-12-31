from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://10.0.16.206:5501/test.html")

    time.sleep(2)

    nameTextBox = driver.find_element(By.ID,"username")
    nameTextBox.send_keys("admin")
    time.sleep(2)
    passTextBox = driver.find_element(By.ID,"password")
    passTextBox.send_keys("12345")
    time.sleep(2)
    loginButton = driver.find_element(By.ID,"login_button")
    loginButton.click()

    time.sleep(5)
    actualTitle = driver.title
    if actualTitle == "Dashboard":
        print("TEST PASS")
    else:
        print("FAIL")

    driver.back()
    time.sleep(2)
    nameTextBox = driver.find_element(By.ID,"username")
    nameTextBox.clear()
    nameTextBox.send_keys("admi")
    time.sleep(2)
    passTextBox = driver.find_element(By.ID,"password")
    passTextBox.send_keys("12345")
    time.sleep(2)
    loginButton = driver.find_element(By.ID,"login_button")
    loginButton.click()
    
    errorMsg = driver.title
    if errorMsg == "Invalid username or password":
        print("Test Pass")
    else:
        print("Fail")

finally:
    driver.quit()