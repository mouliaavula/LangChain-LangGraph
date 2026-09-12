from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age:int
    course:str
    

student = Student(
    name ="Mouli",
    age = 44,
    course = 100 #"Python", if we give wrong type pydantic validate it , this gives error
)

#o/p:pydantic_core._pydantic_core.ValidationError: 1 validation error for Student course

print(student)
print(student.name)
print(student.age)
print(student.course)