class Person:
    def __init__(self,name,age,address):
        self.__name = name #private
        self._age = age #protected
        self.address = address#public
    def __dispaly(self):#private method
        print("Name=",self.__name)

P = Person('vishnu',28,'hyd')
print(P.address)
print(P._age)
print()