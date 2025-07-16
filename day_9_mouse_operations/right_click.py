import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
service_obj=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service_obj,options=ops)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
act=ActionChains(driver)
driver.find_element(By.XPATH,"//a[@class='reference internal ' and normalize-space()='Demo gallery']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Simple Context Menu' and @class='reference internal current']").click()
right_click=driver.find_element(By.XPATH,"//span[normalize-space()='right click me']")
act.context_click(right_click).perform()
driver.find_element(By.XPATH,"//span[normalize-space()='Delete']").click()
alert=driver.switch_to.alert
time.sleep(10)
alert.accept()
time.sleep(10)