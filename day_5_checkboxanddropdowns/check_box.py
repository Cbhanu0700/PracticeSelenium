import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait=WebDriverWait(driver,15)
driver.get("https://total-qa.com/checkbox-example/")
driver.maximize_window()

checkboxes=driver.find_elements(By.XPATH,"//input[@name='chk']")
# checkboxes[0].click()#by index
# time.sleep(10)
#approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()
#approach 2
# for checkbox in checkboxes:
#     checkbox.click()
#     wait.until(lambda driver:checkbox.is_selected())

#3)select multiple check boxes by choice
# for checkbox in checkboxes:
#     if checkbox.get_attribute('id')=='c_bs_2':
#       checkbox.click()

#4)select last two check boxes
# selection=len(checkboxes)
# check_boxes_to_be_selected=selection-2
# for i in range(check_boxes_to_be_selected,selection):
#     checkboxes[i].click()

# 5)select first two checkboxes
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()
time.sleep(10)
   # 6) clear all checkboxes
for i in range(len(checkboxes)):
    if checkboxes[i].is_selected():
        checkboxes[i].click()

time.sleep(15)