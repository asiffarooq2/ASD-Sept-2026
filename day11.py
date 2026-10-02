# class Parent:
#     company="Microsoft"
#     def display(self):
#         print("This is Display Function")

# class Child(Parent):
#     age=50
#     def show(self):
#         print("This is Display Function")

# class Grandson(Child):
#     def hello(self):
#         print("Grandson")
# obj=Grandson()
# obj.display()
# obj2=Child()
# obj2.display()
# print(obj2.company)

# class First:
#     def __init__(self):
#         print("Parent Class Constructor Called")
#     def show(self):
#         print("Parent show")
# class Second(First):
#     def __init__(self):
#         super().__init__()
#         print("Child Class Constructor Called")
#     def show(self):
#         super().show()
#         print("Child show")
        
# obj1=Second()
# obj1.show()

# class Dog:
#     def sound(self):
#         print("Bark")
# class Cat:
#     def sound(self):
#         print("Meow")
# for animal in (Dog(), Cat()):
#     animal.sound()
# animal1=Dog()
# animal2=Cat()

# class Parent:
#     company="Microsoft"  #Public Variable
#     _age=50  #Protected Variable
#     __marks=589  #Private Variable
#     def display(self):
#         print("This is Display Function")
# obj=Parent()
# print(obj.company)
# print(obj._age)
# print(obj.__marks)
# obj.display()

# import os
# os.remove("asif.txt")

class Parent:
    company="Microsoft"  

    @classmethod
    def change_company(cls,name):
        cls.company=name

    @staticmethod  #Decorator
    def display():
        print("This is Display Function")
Parent.change_company("HCL")
print(Parent.company)
# obj1=Parent()
# print(obj1.company)
# obj1.change_company("Dell")
# print(obj1.company)
# obj1.display()
# obj2=Parent()
# obj2.display()