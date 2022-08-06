import csv
req_file = "C:\\Data\\newinfo.csv"
fo = open(req_file,'r')
content = csv.reader(fo,delimiter="|")
#print(list(content))#prints the content in one list
for each in content:
    print(each)
fo.close()