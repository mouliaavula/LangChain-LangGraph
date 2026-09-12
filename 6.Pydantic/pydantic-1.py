from pydantic import BaseModel

# Student(BaseModel):  means Student extending parent BaseModel
# the below is we are defining schema/structure
class Student(BaseModel):
    name:str
    age:int
    course:str
    
# we are create object for student class
student = Student(
    name ="Mouli",
    age = 44,
    course = "Python"
)
# BaseModel is rich class , so it has overriden __str__ so print(student)     gives meaningful info

print(student)
#o/p:name='Mouli' age=44 course='Python' 
# But this is not possible for user defined class, to get this we have to override __str__ in user defined class
print(student.name)
print(student.age)
print(student.course)