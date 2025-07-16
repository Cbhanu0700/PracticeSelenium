import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=ops)
driver.implicitly_wait(10)
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()

# #1)scroll down the page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.pageYOffset;")
# time.sleep(9)
# print(value)

#2)Scroll element till webelement is present
# web_element=driver.find_element(By.XPATH,"//span[text()='Mauritius']")
# driver.execute_script("arguments[0].scrollIntoView();",web_element)
# value=driver.execute_script("return window.pageYOffset;")
# time.sleep(9)
# print(value)


#3)Scroll element till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(9)

#4)Scroll element till up
driver.execute_script("window.scrollBy(0,- document.body.scrollHeight)")