# In python we have pipe | operator, bitwise OR operator
# s1 | s2 ==> sets union operator s1.union(s2)
# To override pipe | operator we have to implement magic method
# __or__()

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    # for example we are defining below method to return substraction
    def __or__(self,other):
        return self.salary - other.salary
e1 = Employee("Mouli",30000)
e2 = Employee("Neethu",20000)
print(e1 | e2)