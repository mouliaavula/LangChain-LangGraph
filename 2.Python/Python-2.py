class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def __str__(self):
        return "I am student with name : "+self.name+" and rollno "+str(self.rollno)
    def eat(self):
        print("I am "+self.name+ " eating ....")
s1 = Student("Mouli",100)
s2 = Student("Neethu",200)
print(s1) # s1 passed as self implicitly
s1.eat()
print(s2)
s2.eat()