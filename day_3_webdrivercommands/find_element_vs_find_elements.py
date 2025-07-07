import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.nopcommerce.com/login")
############## FInd element ###########
#1)Locator matching with single webelement
# webelement=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# webelement.send_keys("Apple macbook")

# 2) locator matching multiple elements
# web_element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(web_element.text)
# time.sleep(7)

#3) if the webelement is not present in web
# console willl throw noSuchElementException
# web_element=driver.find_element(By.LINK_TEXT,"Log")
# web_element.click()
# time.sleep(7)

############## FInd element ###########
#1)Locator matching with single webelement
# element=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(element))
# print(element[0].send_keys("Mobile"))
# time.sleep(8)


# 2) locator matching multiple elements
# web_element=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(web_element))
# for i in web_element:
#     print(i.text)
# time.sleep(7)

#3) if the webelement is not present in web
# console willl throw noSuchElementException
web_element=driver.find_elements(By.LINK_TEXT,"Log")
print(len(web_element))
time.sleep(7)
