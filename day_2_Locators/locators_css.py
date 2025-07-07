import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.CSS_SELECTOR,"input#Email").send_keys("admin@yourstore.com")
driver.find_element(By.CSS_SELECTOR,"input.password").clear()
driver.find_element(By.CSS_SELECTOR,"input.password").send_keys("admin")
# driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()
driver.find_element(By.CSS_SELECTOR,"button.button-1[type=submit]").click()
time.sleep(10)
