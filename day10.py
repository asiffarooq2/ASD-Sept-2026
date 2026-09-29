# class Student:
#     school="R.P School"
#     def __init__(self,name,qualf,exp):
#         self.exp=exp
#         self.qualf=qualf
#         self.name=name
#         print("Constructor Called...")
#     def display(self):
#         # print("Welcome to Object Oriented Programming")
#         print(f"My name is {self.name},MY Qualification is {self.qualf} and I have {self.exp} of teaching experience")
# asif=Student("Asif Farooq","MCA","10 years")
# asif.display()
# deepak=Student("Deepak","BCA","5 years")
# deepak.display()
# asif.school="Burn Hall"
# print(asif.school)
# print(deepak.school)
# nomesh=Student()
# print(asif.school)
# asif.display()

# Create a class for Employee with salary, name.
# Make a method to increase salary by 10%
class Employee:
    company="Microsoft"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def increase_salary(self):
        per=self.salary*(10/100)*100
        self.salary+=per
    def display(self):
        print(f"The name of employee is {self.name} and his salary is {self.salary}.He is working in company {self.company}")
obj1=Employee("Asif",45000)
obj2=Employee("Deepak",65000)
obj1.increase_salary()
obj1.display()
obj2.display()

