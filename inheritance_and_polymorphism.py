"""
Project:OOP Inheritance and Polymorphism Demonstration
Purpose:Demonstration class inheritance (Student to GradStudents) and dynamic Polymorphism across different objects (Student, GradStudents,Employee).
Key Concept:Method Overriding,Polymorphism,Class Variables,Subclassing, and polymorphic Iteration.
Usage:Serves as an execution script to show how diverse Classes share comman interface mothodslike printFullName().
"""
class Student:
    total_Students=0
    def __init__(self,first,last,email,phone):
        self.first=first
        self.last=last
        self.email=email
        self.phone=phone
        Student.total_Students+=1


    def printFullName(self):
        print(self.first+""+self.last)

    def ChangePhone(self,newPhone):
        self.phone=newPhone

class GradStudents(Student):
    total_grad_Students=0
    def __init__(self, first, last, email, phone,degree):
        super().__init__(first, last, email, phone)
        self.degree=degree
        GradStudents.total_grad_Students+=1

    def printDegInfo(self):
        print("{} is pursuing {} degree".format(self.first,self.degree))

s1=Student("bushra","bashir","bushra.bashiremail.com",123456)
s2=Student("irha","ahmad","irha.ahmademail.com",789012)
gs1=GradStudents("atika","basheer","atika.basheeremail.com",345678,"PHD")

gs1.printFullName()
print(gs1.total_Students)
print(gs1.total_grad_Students)
gs1.printDegInfo()
    
#print(issubclass(GradStudents,Student))
#print(issubclass(Student,GradStudents))

class Employee:
    def __init__(self,fname,lname,address,age):
        self.fname=fname
        self.lname=lname
        self.address=address
        self.age=age

    def printFullName(self):
        print("Empolyee full name is {} {}".format(self.fname,self.lname))

empl=Employee("sanina","bashir","main st",30)
lst=[empl,s1,gs1]
for i in lst:
    i.printFullName()






        
