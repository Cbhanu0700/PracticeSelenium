import time
from typing import KeysView

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
location=os.getcwd()
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
service_obj=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service_obj,options=ops)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
registration_link=Keys.CONTROL+Keys.ENTER
driver.find_element(By.LINK_TEXT,"Register").send_keys(registration_link)
time.sleep(5)

