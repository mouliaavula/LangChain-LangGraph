# Field: Sometime field names alone may not enough so we can provide field description 
# so that LLM can understand more clearly 

'''
In Pydantic, Field() is used to give extra information, rules, or constraints to a field.
BaseModel → defines the structure
Type annotation → defines the data type
Field() → adds rules, defaults, descriptions, and metadata
'''

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
