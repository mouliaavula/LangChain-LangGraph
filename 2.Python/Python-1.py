class Student:
    def __init__(self,name,rollno):
        self.name  = name
        self.rollno = rollno
    def __str__(self):
        return "I am student with name: "+self.name+" and Roll no: "+str(self.rollno)
    def eat(self):
        print("I am : "+self.name+" eating ....")
s = Student("Mouli",101)
print(s)
s.eat()
    