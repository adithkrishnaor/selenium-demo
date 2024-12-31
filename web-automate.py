from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://127.0.0.1:5500/index.html")
    time.sleep(3)
    check_element = driver.find_element(By.TAG_NAME, "h1")
    if check_element.text.strip() == "FISAT":
        nameTextBox = driver.find_element(By.NAME,"fname")
        nameTextBox.send_keys("Adith")
        time.sleep(5)
        print("PASS")
    else:
        print("FAIL")

finally:
    driver.quit()