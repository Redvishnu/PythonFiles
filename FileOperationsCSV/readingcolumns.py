import csv
req_file = "C:\\Data\\newinfo.csv"
fo = open(req_file,'r')
content = csv.reader(fo,delimiter="|")
print(list(content))
print(len(list(content)))
#header = next(content)
#print(header)
print("the no of rows are:",len(list(content))-1)