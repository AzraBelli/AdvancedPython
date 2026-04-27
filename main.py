#Section1: DECORATORS
from unittest import result

print("="*60)
print("Section 1:DECORATOR")
print("="*60)


def my_decorator(func):
    def wrapper():
        print("wrapper function executed")
        func()
        print("wrapper function executed")

    return wrapper

@my_decorator
def hello_world():
    print("hello world")
hello_world()


#Section2:Property Decorators
print("="*60)
print("Section 2:Property Decorators")
print("="*60)

#data validation,private(__)/public(encapsulation)
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    #getter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value=="Azra":
            print("Azra not accepted")
        else:
            self.__name = value
        #if we want that we can change and manipulation code



azra=Person("Azra",32)
print(azra.name)
azra.name="Azra B"
print(azra.name)#it is  working because it has  setter


