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
    preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
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
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf ")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)
    ops.set_preference("browser.download.dir", download_path)
    # ✅ Set actual path
    ops.set_preference("pdfjs.disabled",True)
    # ✅ Use Firefox driver, not Edge
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=ops)
    return driver

driver = chrome_setup()
driver.get("https://sample-videos.com/download-sample-pdf.php")  # better for .doc download

# Example for downloading a .doc file (update XPath as needed)
driver.find_element(By.XPATH, "//a[@class='download_pdf']").click()