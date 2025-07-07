"""
1) Open Web Browser(Chrome/firefox/IE).
2) Open URL  https://admin-demo.nopcommerce.com/login
3) Provide Email  (admin@yourstore.com).
4) Provide password  (admin).
5) Click on Login.
6) Capture title of the dashboard page.(Actual title)
7) Verify title of the page: "Dashboard / nopCommerce administration" (Expected)
8) close browser
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
print(driver.title)
if driver.title=='nopCommerce demo store. Login':
    print("Test Case Passed")
else:
    print("Test Case Failed")
time.sleep(10)