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
my_dict=driver.get_cookies()

print(f"length of cookies:",len(my_dict))

#Print details of all cookies
# for cookie in my_dict:
#     print(cookie.get('expiry'),":",cookie.get('value'))

# #add new cookie
# driver.add_cookie({"name": "mycookie", "value": "123456"})
# print(f"length of cookies:",len(driver.get_cookies()))


#delete a cookie
driver.delete_cookie('mycookie')
driver.delete_all_cookies()