from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.snapdeal.com/")
print(driver.current_url)
driver.get("https://amazon.com")
print(driver.current_url)

driver.back()
print(driver.current_url)
driver.forward()
print(driver.current_url)
driver.refresh()
print(driver.current_url)