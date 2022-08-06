import csv
req_file = "C:\\Data\\demo.csv"
fo = open(req_file,'w',newline="")
content = csv.writer(fo,delimiter=",")
'''content.writerow(['S,no','Name','Age'])
content.writerow(['1','Vishnu','46'])'''
my_data = [['s.no','name','age'],[1,'john',23],[2,'vishnu',30]]
content.writerows(my_data)
fo.close()