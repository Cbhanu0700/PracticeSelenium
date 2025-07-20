import pyodbc

# Check available ODBC drivers
print(pyodbc.drivers())

# Connect to the database
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 13 for SQL Server};"
    "SERVER=DGA1app39AXODV,1433;"
    "DATABASE=Attends;"
    "UID=sa;"
    "PWD=abc-123"
)

# Create a cursor object
curs = conn.cursor()

# # INSERT
# insert_sql = "INSERT INTO putimeend VALUES (?, ?, ?)"
# insert_values = (2, 29216, '2024-01-11 00:01:43.000')
# curs.execute(insert_sql, insert_values)

# UPDATE
# ✅ Replace col1, col2, and putime with actual column names in your table
# update_sql = "UPDATE putimeend SET Order_ID = 29219 WHERE putime = '2024-01-11 00:01:43.000'"
# curs.execute(update_sql)

# DELETE
delete_sql = "DELETE FROM putimeend WHERE putime ='2024-01-11 00:01:43.000'"
curs.execute(delete_sql)

# Commit and close
conn.commit()
conn.close()

print("Finished....")
