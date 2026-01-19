"""class Student:                  #class
    name="Kshitij"
    likes="Music"
    
a=Student()                     #object of class
a.name="Kitty"
print(a.name,a.likes)

b=Student()
c=Student()
print(b.name,c.name)
"""
"""class Clg:
    name="ATSS"
    place="Chinchwad"
    def clgg(self):
        print(f"{self.name} clg is in {self.place}")

a=Clg()
a.clgg()"""


#parametarized constructor
class Clg:
    def __init__(self,name,place): 
        self.name=name
        self.place=place
    def info(self):
        print(f"{self.name} is from {self.place}")
a=Clg("kshitij","Pune")
b=Clg("Durvas","Chikhli")
a.info()
b.info()

#default constructor
class School:
    def __init__(self):
        print("My name is Kshitij")
a=School()

#create student class that takes name and marks of 3 subjects as a arg in constructor. Then create an method to print an avg
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print(f"{self.name} has {self.marks} marks")
    def avg(self):
        sum=0 
        for i in self.marks:
            sum+=i
        print(f"{self.name} your avg marks are :",sum/3)
std1=Student("Kshitij",[28,29,40])
std1.avg()

##create student class that takes name and marks of 3 subjects as a arg in constructor. Then create an method to print an avg

class Std:
    @staticmethod
    def clg(name):
        print(name)
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print(f"{self.name} your avg is :",sum/len(self.marks))
s1=Std("KK",[28,29,40])
s1.avg()
s1.clg("DYP")

class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no

    def debit(self,amt):
        self.balance-=amt
        print("Amount debited:",amt)
        print("Amount Remaining:",self.balance)

    def credit(self,amt):
        self.balance+=amt
        print("amount credited:",amt)
        print("Total Amount Remaining",self.balance)
        
pr1=Account(10000,72671638)
print("Current balance is:",pr1.balance)
print("Acc no is:",pr1.acc_no)
pr1.debit(100)
pr1.credit(2000)

