import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.deadlinkcity.com/")
links=driver.find_elements(By.XPATH,"//a")
count=0
for link in links:
    url=link.get_attribute('href')
    try:
     res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url," is broken")
        count +=1
    else:
        print(url, "is valid")

print("total no of Broken links:",count)