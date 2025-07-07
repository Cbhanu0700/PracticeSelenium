import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(5)
alert=driver.switch_to.alert
print(alert.text)
alert.send_keys("Welcome")
# alert.accept()
alert.dismiss()
time.sleep(20)
