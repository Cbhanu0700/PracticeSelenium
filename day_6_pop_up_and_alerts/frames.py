import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys("India")
time.sleep(10)
driver.switch_to.frame("courses-iframe")
get_text=driver.find_element(By.XPATH,"//a[text()='VIEW ALL COURSES']").text
print(get_text)
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//input[@id='autocomplete']").clear()
time.sleep(15)

