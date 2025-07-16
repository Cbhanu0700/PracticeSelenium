import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
ops=webdriver.EdgeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=Service(EdgeChromiumDriverManager().install()),options=ops)
driver.get("https://text-compare.com/")
driver.maximize_window()
driver.implicitly_wait(10)
input_1=driver.find_element(By.ID,"inputText1").send_keys("Welcome")
input_2=driver.find_element(By.ID,"inputText2")

"""
CTRL+A
CTRL+c
tab
CTRL+v
"""
#CTRL+A
act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#release the control key
#CTRL+c
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
#Tab
act.send_keys(Keys.TAB)
#CTRL+v
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(5)
