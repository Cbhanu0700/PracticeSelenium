import time

from selenium import webdriver
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
driver.get("https://www.nopcommerce.com/en?srsltid=AfmBOoqqgePggWwqW9FmkNXWBcVIuDwaDa4__usRd-UGtWLODgKIM8Rp")
# driver.save_screenshot(os.path.join(location,"Sample.png"))
driver.get_screenshot_as_file(location+"\\sample_2.png")