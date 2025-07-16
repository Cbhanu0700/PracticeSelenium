from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
ops.add_argument("--start-maximized")
# Optional: block images for speed
# prefs = {"profile.managed_default_content_settings.images": 2}
# ops.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=ops)
driver.implicitly_wait(10)

# Navigate
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

# Wait for sliders
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.ui-slider-handle")))

# Locate sliders
max_slider = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)")
min_slider = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(2) > span:nth-child(3)")

# Print positions
print(f"Before Moving slider: {max_slider.location}, {min_slider.location}")

# Move min slider
ActionChains(driver).drag_and_drop_by_offset(min_slider, 100, 0).pause(1).perform()
ActionChains(driver).drag_and_drop_by_offset(max_slider, -59, 0).pause(1).perform()
# Print positions again
print(f"After Moving slider: {max_slider.location}, {min_slider.location}")
