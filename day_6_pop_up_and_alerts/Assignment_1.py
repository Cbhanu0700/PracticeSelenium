import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
main_window=driver.current_window_handle
driver.implicitly_wait(15)
driver.maximize_window()
driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("selenium")
driver.find_element(By.CLASS_NAME,"wikipedia-search-button").click()
# Store existing windows before clicking any result
existing_windows = set(driver.window_handles)
search_results=driver.find_elements(By.XPATH,"//a[contains(text(),'Selenium')]")
for search in search_results:
    search.click()
    time.sleep(1)  # Give time for the new tab to open

    # Identify the newly opened window
new_windows = driver.window_handles
for new_window in new_windows:
 driver.switch_to.window(new_window)
 print(driver.title)
 if "biology" in driver.title.lower() or "disulfide" in driver.title.lower():
     print("Closing tab:", driver.title)
     driver.close()

time.sleep(10)