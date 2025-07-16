import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

location=os.getcwd()
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    ops=webdriver.ChromeOptions()
    ops.add_argument("--disable-notifications")
    preferences={"download.default_directory":location}
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Edge(service=Service(ChromeDriverManager().install()),options=ops)
    return driver

def edgesetup():
    from selenium.webdriver.edge.service import Service
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    ops=webdriver.EdgeOptions()
    ops.add_argument("--disable-notifications")
    preferences={"download.default_directory":location}
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=ops)
    return driver

def firefox_setup():
    download_path = os.getcwd()  # ✅ Use actual path

    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)
    ops.set_preference("browser.download.dir", download_path)  # ✅ Set actual path

    # ✅ Use Firefox driver, not Edge
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=ops)
    return driver

driver = firefox_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")  # better for .doc download

# Example for downloading a .doc file (update XPath as needed)
driver.find_element(By.XPATH, "(//a[contains(text(),'Download sample DOC file')])[1]").click()