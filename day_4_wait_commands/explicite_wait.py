from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/")
mywait=WebDriverWait(driver,10,ignored_exceptions=[Exception])
searchlink=mywait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".oxd-text.oxd-text--h5")))
print(searchlink.text)