import pyodbc
import pandas as pd
import os
from datetime import datetime
from plyer import notification
import csv
db = pyodbc.connect("Driver={SQL Server};"
                    "Server=DESKTOP-JSJF54F\VISHNU_07_SERVER;"
                    "Database=vishnu;"
                    "Trusted_connection=yes;")
sql_query = pd.read_sql_query("select ID,Role,Name, Sal from Emp1", db)  # here, the 'conn' is the variable that contains your database connection information from step 2
dataset = pd.DataFrame(sql_query)
#dataset.to_csv(r'C:\\Files.csv','.csv', index=False)
print(dataset)
dataset.to_csv(r'C:\Users\Admin\PycharmProjects\exceldoc\sql_data.csv', index = False)
notification.notify(title="report status!!!", message=f"sales saved.\n",timeout = 10)
#with open(r'C:\Users\Admin\PycharmProjects\exceldoc\'sql_data_25-Jun-22165344.csv', 'r') as csv_file:


