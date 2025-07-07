import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
#self
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Nestle India')]/self::a").text
#parent
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Nestle India')]/parent::td").text
#child
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Nestle India')]/ancestor::tr/child::td")
# print(len(text_msg))

#Ancestor
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Nestle India')]/ancestor::tr").text
# print((text_msg))

#descendent
#Ancestor
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Nestle India')]/ancestor::tr/descendant::td[2]").text
# print((text_msg))

#Following
# text_msg=driver.find_elements(By.XPATH,"//a[c ontains(text(),'Nestle India')]/ancestor::tr/following::*")
# print(len(text_msg))

#following sibiling
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Nestle India')]"))
)

# Locate following rows
text_msg = driver.find_elements(By.XPATH, "//a[contains(text(),'Nestle India')]/ancestor::tr/following-sibling::*")
print(len(text_msg))