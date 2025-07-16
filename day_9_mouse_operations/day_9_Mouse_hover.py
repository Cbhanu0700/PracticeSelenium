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
driver.get("https://jqueryui.com/menu/")
driver.maximize_window()
action=ActionChains(driver)
frame=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(frame)
hover_1=driver.find_element(By.XPATH,"//*[text()='Music']")
hover_2=driver.find_element(By.XPATH,"//*[text()='Rock']")
hover_3=driver.find_element(By.XPATH,"//*[text()='Alternative']")

action.move_to_element(hover_1).pause(1).move_to_element(hover_2).pause(1).move_to_element(hover_3).click().perform()

time.sleep(10)