

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10 )
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//textarea[@name='q']").send_keys("selenium")
driver.find_element(By.XPATH,"//textarea[@name='q']").submit()
webelement=driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

