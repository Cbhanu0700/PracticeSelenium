import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(15)
#1)Read all no of rows and coloumns
# headers=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
# print("Total no of headers:",len(headers))
rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
# print("Total no of rows:",len(rows))
coloumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td"))



# #2)Read specific row and column data
# row_data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[2]").text
# print(row_data)
# coloumn_data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[3]/td[1]").text
# print((coloumn_data))


#2)Read specific row and column data
# row_data=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
# for row in row_data:
#     print(row.text)


#3)Read all rows and columns data
#
# for r in range(2,rows+1):
#     for c in range(1,coloumns+1):
#      data=driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[{r}]/td[{c}]").text
#      print(data,end=" ")
#     print()


#Read data based on condition(List books name whose author is mukesh
for r in range(2,rows+1):
    author_name = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{r}]/td[2]").text
    if author_name=="Mukesh":
        bookname=driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{r}]/td[1]").text
        price = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{r}]/td[4]").text
        print(bookname,price)