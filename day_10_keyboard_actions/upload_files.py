import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
ops=webdriver.EdgeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=ops)
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
driver.find_element(By.ID,"file-upload").send_keys("C:\\Users\\cprakash\\OneDrive - Aptean-online\\Desktop\\SrvanyInstructions.docx")
time.sleep(5)
