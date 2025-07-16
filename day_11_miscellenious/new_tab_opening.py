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
driver.switch_to.new_window('tab')
driver.get("https://www.orangehrm.com/")
time.sleep(5)


