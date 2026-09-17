class Student:
    def __init__(self,name,rollno):
        self.name  = name
        self.rollno = rollno
    def __str__(self):
        return "I am student with name: "+self.name+" and Roll no: "+str(self.rollno)
    # To every method self is passed implicitly
    def eat(self):
        print("I am : "+self.name+" eating ....")
s = Student("Mouli",101)
# if we do not override __str__ then print(s) print as  
# <__main__.Student object at 0x000001B2A4ACB380>
print(s)
#o/p: I am student with name: Mouli and Roll no: 101
# with override __str__
s.eat()
# str() converts a value into a string representation.
# Any value → str() → String