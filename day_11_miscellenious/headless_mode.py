import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

ops=webdriver.ChromeOptions()
ops.headless=True
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://demo.nopcommerce.com/login")
element=driver.find_element(By.XPATH,"//input[@id='Email']")
element.clear()
element.send_keys("abc@gmail.com")
print("result:",element.text)
print("result:",element.get_attribute('value'))
time.sleep(5)
