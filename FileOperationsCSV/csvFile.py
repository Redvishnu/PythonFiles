import csv
req_file = "C:\\Data\\newinfo.csv"
fo = open(req_file,'r')
content = fo.readlines()#with readlines we are getting entire line in one line only, i need not get like that
#because in csv  i need to get it in terms of columns
for each in content:
    print(each.strip("\n"))
fo.close()
print()
print()
req_file = "C:\\Data\\news.csv"
fo = open(req_file,'r')
content = csv.reader(fo)#with csv reader we will convert data into columns
#it will print each line in the form list.list means number of values , seperate values
for each in content:
    print(each)
#print(content)- we cant print conetnt directly because it is an object.inside of that contains rows and each
# row contains cloumns

#without csv reader also we can  convert your data into columns
fo = open(req_file,'r')
content = fo.readlines()
for each in content:
    print(each.strip("\n").split(","))
fo.close()






