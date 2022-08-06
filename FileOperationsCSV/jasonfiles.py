import json
req_path = "C:\\Data\\hdfc.txt"
fo = open(req_path,'r')
print(fo.read())
print(json.load(fo))
fo.close()


my_dict = {'Name':'vishnu','skills':['python','AWS','SQL']}
req_file = "path"
fo = open(req_file,'w')
json.dump(my_dict,fo,indent=3)
fo.close()