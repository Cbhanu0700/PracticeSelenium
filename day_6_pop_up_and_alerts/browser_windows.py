import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# windowid=driver.current_window_handle
# print(windowid)#F077CCB26376896541524629A9DA4D6D
# #5FDA8D94A851A325A793CAF6365B31C6
time.sleep(10)
driver.find_element(By.XPATH,"//a[@href='http://www.orangehrm.com']").click()
time.sleep(10)
window_ids=driver.window_handles
# parent_windowid=window_ids[0]
# child_windowid=window_ids[1]
# print(parent_windowid,child_windowid)
# driver.switch_to.window(parent_windowid)
# driver.find_element(By.NAME,"username").send_keys("Admin")
# for i in window_ids:
#     driver.switch_to.window(i)
#     print(driver.title)

#Closing soecific browsers
for i in window_ids:
    driver.switch_to.window(i)
    if driver.title=="OrangeHRM":
        driver.close()
        time.sleep(10)
time.sleep(10)