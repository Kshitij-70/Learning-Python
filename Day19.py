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