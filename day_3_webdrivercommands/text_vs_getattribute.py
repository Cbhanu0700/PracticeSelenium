import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.nopcommerce.com/login")
element=driver.find_element(By.XPATH,"//input[@id='Email']")
element.clear()
element.send_keys("abc@gmail.com")
print("result:",element.text)
print("result:",element.get_attribute('value'))
time.sleep(5)
