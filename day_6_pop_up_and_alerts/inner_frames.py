import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@class='analystic' and @data-toggle='tab' and text()='Iframe with in an Iframe'] ").click()
outer_frame=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)

inner_frame=driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")
driver.switch_to.parent_frame()
time.sleep(10)