#private method and attributes
class Std:
    __name="Kshitij"

    def nam(self):              
        return self.__name  #we can access private methods only inside class and not from outside

std1=Std()
print(std1.nam())

#inheritance
class Father:
    @staticmethod
    def car():
        print("Has Car")

    @staticmethod
    def bike():
        print("Has Bike")

class Son(Father):
    def __init__(self,aeroplane):
        self.aeroplane=aeroplane

s1=Son("aeroplane")
print(s1.aeroplane)
print(s1.bike())

class Car:
    @staticmethod
    def start():
        print("Car Started")

class Lambo(Car):
    def __init__(self,name):
        self.name=name

per1=Lambo("Urus")
print(per1.name)
print(per1.start())

#multi level inheritance
class Animal:
    def __init__(self,eat):
        self.eat=eat

class Lion(Animal):
    @staticmethod
    def car():
        print("Carnivrous")

class Rat(Lion):
    @staticmethod
    def her():
        print("Herbivrous")

ani=Rat("Can Eat")
print(ani.her())
print(ani.car())
        
#super() method
class Humans:
    def __init__(self,type):
         self.type=type

    @staticmethod
    def walk():
        print("Humans can Walk")

class Man(Humans):
    def __init__(self, name,type):
        super().__init__(type)
        self.name=name
        super().walk()

hu=Man("Kshitij","Male")
print(hu.type)

#class method
class Person:
    name="Nonononono"
    @classmethod
    def changeName(cls,name):
        cls.name=name
p1=Person()
p1.changeName("Kshitij")
print(p1.name)