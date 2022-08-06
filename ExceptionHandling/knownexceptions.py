#print(a)-Name Error

#print(10+"value is") -Type error

#print(fo.open(vishnu.txt))-file not found error

try:
    #print(a)
    #print(10+"var")
    #open("vishnu.txt")
     #print(4/0)
     import fabric
except FileNotFoundError:
    print("file not found")
except NameError:
    print("var is not defined")
except TypeError:
    print("unsuported operand")
except ZeroDivisionError:
    print("Divison error")
except Exception as e:
    print(e)
finally:
    print("ill excutes finally")