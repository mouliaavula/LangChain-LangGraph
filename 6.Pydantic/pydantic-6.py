from pydantic import BaseModel
# for optional fields instead of none we can also pass some other values but it should 
# match field type

class Student(BaseModel):
    name:str
    age : int
    course : str | None = 'Langchain' # if we pass 10 gives error
#==========default value not used as we pass value for course    
# s = Student(name='Neethu',age=8,course='java')
# print(s)

# o/p:name='Neethu' age=8 course='java'

# =============default value used as we do not pass course ===================
s = Student(name = 'Manish',age= 12)
print(s)
#o/p:name='Manish' age=12 course='Langchain'

# name:str | None = None--> optional field with default value None
# name:str | None = 'Mouli'-->optional field with default value mouli not None
# name:str | None = 10 --> optional field with default value 10 but it is wrong type, gives error