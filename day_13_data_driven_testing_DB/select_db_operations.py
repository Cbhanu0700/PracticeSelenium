import pyodbc


conn = pyodbc.connect(
    "DRIVER={ODBC Driver 13 for SQL Server};"
    "SERVER=DGA1app39AXODV,1433;"
    "DATABASE=Attends;"
    "UID=sa;"
    "PWD=abc-123"
)

curs=conn.cursor()
select=curs.execute("Select top 10 *from putimeend order by putime desc")
print(select)
# for row in curs:
#     print(row[0],row[1])
conn.close()