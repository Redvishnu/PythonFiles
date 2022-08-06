import pandas as pd
import  csv

req_file = "C:\\Data\\news.csv"
#re = "Desktop\\SampleSupersto.xlsx"
fo = open(req_file,'r')
df = pd.read_csv(fo)
secondfile = "C:\\Users\\Admin\\PycharmProjects\\exceldoc\\'sql_data.csv"
fo1 = open(secondfile,'r')
df1 = pd.read_csv(fo1)
data  = [df , df1]
df2 = pd.concat(data)
#print(df2)
df2.to_csv(r'C:\Data\concat.csv',index = False)


