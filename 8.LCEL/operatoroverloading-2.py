class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __add__(self,other):
        total = self.salary + other.salary
        return Employee("Dummy",total)
e1 =  Employee("Mouli",10000)
e2 = Employee("Manish",20000)
e3 = Employee("Neethu",30000)
e = e1 + e2 + e3
print(e)
print(e.salary)