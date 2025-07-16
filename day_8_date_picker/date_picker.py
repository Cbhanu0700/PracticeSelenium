import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
service_obj=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service_obj,options=ops)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
wait=WebDriverWait(driver,15)
try:
 element=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='datepicker']")))

except Exception as e:

    print("Exception is :",e)

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
year='2021'
month='March'
date='30'
while True:
    month_select=driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text
    year_select=driver.find_element(By.CLASS_NAME,"ui-datepicker-year").text
    if month_select==month and year_select==year:
        break
    elif int(year_select)>int(year)  or (year_select==year and month_select !=month):
        driver.find_element(By.XPATH, "//a[@title='Prev']").click()

    else:
        driver.find_element(By.XPATH,"//a[@title='Next']").click()#future

driver.find_element(By.XPATH,f"//a[text()='{date}']").click()



time.sleep(10)

