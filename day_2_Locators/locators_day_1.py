import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.nopcommerce.com")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Jewelry").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Appa").click()
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
# driver.find_element(By.ID,"Email").clear()
# driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
# driver.find_element(By.NAME,"Password").clear()
# driver.find_element(By.NAME,"Password").send_keys("admin")
# driver.find_element(By.CLASS_NAME,"button-1").click()
time.sleep(30)

