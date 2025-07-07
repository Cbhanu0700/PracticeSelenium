import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(10)