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
driver.get("https://www.w3schools.com/TAgs/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

# Switch to iframe
driver.switch_to.frame("iframeResult")

# Double click on the button
act = ActionChains(driver)
button = driver.find_element(By.XPATH, "//*[text()='Copy Text']")
act.double_click(button).perform()

# Get copied value
field2 = driver.find_element(By.ID, "field2")
print("Copied text:", field2.get_attribute('value'))  # Should print "Hello World"

# Optional: Close browser
time.sleep(2)
driver.quit()
