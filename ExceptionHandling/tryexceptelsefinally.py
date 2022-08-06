
try:
    a=10
    print(b)
except NameError:
    print("value is not defined")
except Exception as e:
    print(e)
else:
    print("this will excute if there is no exceptions in try block")

finally:
    print("this will excutes allways")