from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age:int
    course:str
#is not valid gives error. In normal python iti is valid as we use constructor in Student class
# but here     
'''
s = Student("Mouli",44,"Python")
print(s)
'''
# o/p: TypeError: BaseModel.__init__() takes 1 positional argument but 4 were given

# =========================================================================================

# Below is valid that is we have to pass in keyword arugments as defined in schema

s = Student(name="Mouli",age=44,course="Python")
print(s)

# Below also valid as we are using keyword arguments order is not important

s1 = Student(age=8, course="GenAI",name="Neeth")
print(s1)
print(type(s1))

