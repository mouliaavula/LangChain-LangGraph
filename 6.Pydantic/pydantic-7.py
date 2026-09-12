# Field: Sometime field names alone may not enough so we can provide field description 
# so that LLM can understand more clearly 

from pydantic import BaseModel,Field

class Student(BaseModel):
    name:str = Field(description='Name of student')
    age:int | None = Field(default=25,description='Age of student')
    course:str | None = 'Langchain'
# ==========all values are passed so no default values are used    
# s = Student(name='mouli',age=44,course='java')
# print(s)
#o/p:name='mouli' age=44 course='java'

#=======only one required name field passed==============
s = Student(name='Sravan')
print(s)
#o/p: name='Sravan' age=25 course='Langchain'