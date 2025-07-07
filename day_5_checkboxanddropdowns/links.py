import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demo.nopcommerce.com/login")
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital downloads").click()
# time.sleep(10)

#Find no of links
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
for link in links:
    print(link.text)