import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj, options=ops)
driver.implicitly_wait(10)

# Navigate
driver.get("https://www.globalsqa.com/demo-site/draganddrop/#google_vignette")
driver.maximize_window()
iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
driver.switch_to.frame(iframe)
act=ActionChains(driver)
source=driver.find_element(By.XPATH,"//h5[text()='High Tatras 3']")
target=driver.find_element(By.ID,"trash")
act.drag_and_drop(source,target).perform()

time.sleep(10)