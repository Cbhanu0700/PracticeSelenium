import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# # driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()
# driver.find_element(By.XPATH,"//input[@id='small-searchterms']").send_keys("Mobiles")
#Absolute xpath
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/fieldset/input").send_keys("India")
time.sleep(20)