import time

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from day_12_data_driven_testing_xcel import excel_utils
from day_12_data_driven_testing_xcel.excel_utils import getRowCount, getColumnCount

ops=webdriver.ChromeOptions()
ops.add_argument('--disable-notifications')
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
driver.implicitly_wait(10)
file="D:\\Book1.xlsx"
workbook=openpyxl.load_workbook(file)
rows_no=excel_utils.getRowCount(file,'Sheet4')
column_no=excel_utils.getColumnCount(file,'Sheet4')
print(rows_no,column_no)

for r in range(2,rows_no+1):

        principle = excel_utils.readData(file, 'Sheet4', r, 1)
        rate_of_interest = excel_utils.readData(file, 'Sheet4', r, 2)
        period_1 = excel_utils.readData(file, 'Sheet4', r, 3)
        period_2 = excel_utils.readData(file, 'Sheet4', r, 4)
        frequency = excel_utils.readData(file, 'Sheet4', r, 5)
        maturity = excel_utils.readData(file, 'Sheet4', r, 6)
        driver.find_element(By.ID, "principal").send_keys(principle)
        driver.find_element(By.ID, "interest").send_keys(rate_of_interest)
        driver.find_element(By.ID, "tenure").send_keys(period_1)
        select_period = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        select_period.select_by_visible_text(period_2)
        frequency_drp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        frequency_drp.select_by_visible_text(frequency)
        driver.find_element(By.XPATH,
                            "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
        actual_maturity_value = driver.find_element(By.XPATH, "//span[@class='gL_27']/strong").text
        if float(maturity) == float(actual_maturity_value):
            print("Test Passed")
            excel_utils.writeData(file, 'Sheet4', r, 8, "Passed")
            excel_utils.fillGreenCOlor(file, 'Sheet4', r, 8)
        else:
            print("Test failed")
            excel_utils.writeData(file, 'Sheet4', r, 8, "Failed")
            excel_utils.fillredColor(file, 'Sheet4', r, 8)
        driver.find_element(By.XPATH, "//img[@class='PL5']").click()
        time.sleep(10)
