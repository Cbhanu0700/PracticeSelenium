import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
service_obj=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service_obj,options=ops)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"oxd-button").click()
driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item' and @href='/web/index.php/admin/viewAdminModule']").click()
status_emp=driver.find_elements(By.XPATH,"//div[text()='Enabled']")
total_no_of_enabled_emp=len(status_emp)
print(total_no_of_enabled_emp)
rows_data=driver.find_elements(By.XPATH,"//div[@class='oxd-table']/div[2]/div[@class='oxd-table-card']")
for row in rows_data:
    print(row.text,end=" ")

time.sleep(10)