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
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
year=2000
month=7
date=13
driver.find_element(By.XPATH,"//input[@id='dob']").click()
while True:
    select_month=driver.find_element(By.XPATH,f"//option[@value='{month}']").click()
    selct_year=driver.find_element(By.XPATH,f"//option[@value='{year}']").click()
    select_date=driver.find_element(By.XPATH,f"//a[@data-date='{date}']").click()
    break

time.sleep(10)
