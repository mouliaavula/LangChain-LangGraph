# Python operator overloading

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    # __add__ is a magic method for + and + behave as you define
    # i.e in below we are defining to return sum of sal from two objects
    # ie. you can define that how your + should behave on call of +
    def __add__(self, other):
        return self.salary + other.salary
e1 = Employee("Mouli",10000)
e2 = Employee("Manish",20000)
e3 = Employee("Neethu",30000)
#print(10+20)
#print("Mouli"+"Aavula")
print(e1+e2)
# this is invoked as e1.__add__(e2)