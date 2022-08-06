try:
    fo = open("vishnu.txt")
    print(fo.read())
    fo.close()
except Exception as e:
    print(e)

my_list = [1,44,56,90]
try:
    print(my_list[5])
except Exception as e:
    print("error in try block is:", e)

print("this code will also exceutes")