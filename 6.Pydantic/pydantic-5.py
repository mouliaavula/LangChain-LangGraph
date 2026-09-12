from pydantic import BaseModel
#pydantic class can contain optional fields
class Student(BaseModel):
    name:str
    age:int
    course:str | None = None

# =======================defalut value not used as we provide value for course==========================================================    
# s = Student(name="Mouli",age=44, course='Python')
# print(s)
# o/p: name='Mouli' age=44 course='Python'

# ====================course not provided so uses default value

s = Student(name='mouli',age=44)
print(s)

#o/p: name='mouli' age=44 course=None
