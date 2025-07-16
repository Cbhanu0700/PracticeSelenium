from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# 1. Tuple – Fixed locator for login button
login_button_locator = (By.ID, "loginBtn")

# 2. Dictionary – Store login credentials and expected dashboard values
test_data = {
    "username": "testuser",
    "password": "password123",
    "expected_buttons": ["Home", "Profile", "Logout"]
}

# 3. List – Store button texts found after login
button_texts = []

# 4. Set – To ensure unique button names are shown (no duplicates)
unique_buttons = set()

# Set up driver (assuming ChromeDriver is in PATH)
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigate to login page
    driver.get("https://example.com/login")  # replace with a real page if needed
    time.sleep(2)

    # Fill login form using dictionary
    driver.find_element(By.ID, "username").send_keys(test_data["username"])
    driver.find_element(By.ID, "password").send_keys(test_data["password"])

    # Click login using tuple locator
    driver.find_element(*login_button_locator).click()
    time.sleep(3)  # wait for dashboard to load

    # Capture all dashboard buttons (List + Set)
    dashboard_buttons = driver.find_elements(By.TAG_NAME, "button")

    for btn in dashboard_buttons:
        text = btn.text.strip()
        button_texts.append(text)
        unique_buttons.add(text)

    # Print captured buttons
    print("All Button Texts (List):", button_texts)
    print("Unique Buttons (Set):", unique_buttons)

    # Compare actual vs expected buttons using Set
    expected_set = set(test_data["expected_buttons"])
    if expected_set.issubset(unique_buttons):
        print("✅ All expected buttons are present.")
    else:
        print("❌ Missing buttons:", expected_set - unique_buttons)

finally:
    driver.quit()
