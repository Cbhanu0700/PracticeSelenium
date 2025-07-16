import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://whatmylocation.com/#google_vignette")
driver.maximize_window()
time.sleep(10)
