import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# #is_displayed
# search_box=driver.find_element(By.ID,"small-searchterms")
# print(search_box.is_displayed())
#
#
# #Is_enabled()
# check_box=driver.find_element(By.CSS_SELECTOR,"#Newsletter")
# print(check_box.is_enabled())
# check_box.click()
# print(check_box.is_enabled())

#Is_selected
check_box=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(check_box.is_selected())
check_box.click()
print(check_box.is_selected())
time.sleep(20)