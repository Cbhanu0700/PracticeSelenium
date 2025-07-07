import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://practice.expandtesting.com/dropdown")
drop_down=driver.find_element(By.CSS_SELECTOR,"#country")
drpcountry=Select(drop_down)
# drpcountry.select_by_visible_text("Angola")
# drpcountry.select_by_value('AI')
# drpcountry.select_by_index(5)


#Capture all the options and print them
names=drpcountry.options
print(len(names))
# country_name=driver.find_elements(By.XPATH,"//option")
# count=0
# for country in country_name:
#     print(country.text)
#     count +=1
# print("total no of options are:",count)
time.sleep(10)