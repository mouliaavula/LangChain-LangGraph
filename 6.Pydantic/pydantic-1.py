from pydantic import BaseModel

# Student(BaseModel):  means Student extending parent BaseModel
# the below is we are defining schema/structure
class Student(BaseModel):
    name:str # called as annotations i.e declaring field type is called annotation
    age:int
    course:str
    
# create object for student class
student = Student(
    name ="Mouli",
    age = 44,
    course = "Python"
)
# BaseModel is rich class , so it has overridden __str__ so print(student)     gives meaningful info

print(student)
#o/p:name='Mouli' age=44 course='Python' 
# But this is not possible for user defined class, to get this we have to override __str__ in user defined class
print(student.name)
print(student.age)
print(student.course)


"""
Pydantic is a Python library used to define the structure of data and validate that data.

In LangChain, it is important because LLMs return human-readable/free flow text,
while LangChain applications often need structured

Ex: Give me the student's name and age.

LLM Answer: The student is Mouli and he is 44 years old.

That's human-readable, but your Python program may want:
{
    "name": "Mouli",
    "age": 44
}

"""