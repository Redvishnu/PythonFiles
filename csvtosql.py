import pandas as pd
import pyodbc
data = pd.read_csv (r'C:\Users\Admin\PycharmProjects\exceldoc\'sql_data.csv')
df = pd.DataFrame(data)

print(df)
conn = pyodbc.connect("Driver={SQL Server};"
                    "Server=DESKTOP-JSJF54F\VISHNU_07_SERVER;"
                    "Database=vishnu;"
                    "Trusted_connection=yes;")
cursor = conn.cursor()
df1 = cursor.execute('''select * from products''')
print(df1)
cursor.execute('''
		CREATE TABLE products (
			ID int,
			Role nvarchar(50),
			Name varchar(50),
			Sal int
			)
               ''')

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO products (ID, Role, Name,Sal)
                VALUES (?,?,?,?)
                ''',
                row.ID,
                row.Role,
                row.Name,
                row.Sal
                )
conn.commit()


print(df1)
