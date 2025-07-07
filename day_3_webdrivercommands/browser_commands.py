import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(20)
driver.find_element(By.XPATH,"//a[@href='http://www.orangehrm.com']").click()
# driver.close()
time.sleep(5)
driver.quit()
time.sleep(5)
input("Press Enter to exit...")
