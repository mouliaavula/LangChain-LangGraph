from pydantic import BaseModel,ValidationError

class Student(BaseModel):
    name:str
    age:int
    course:str

# pydantic will perform validations against schema
#===Field missing============================================================================
# s = Student(name='Mouli',age=44)

#o/p:
'''
pydantic_core._pydantic_core.ValidationError: 1 validation error for Student
course
  Field required [type=missing, input_value={'name': 'Mouli', 'age': 44}, input_type=dict]
'''
# ===============Wrong filed type==========================================================
# s = Student(name='Mouli',age=44, course=10)

# o/p:
'''
pydantic_core._pydantic_core.ValidationError: 1 validation error for Student
course
  Input should be a valid string [type=string_type, input_value=10, input_type=int]
'''

# ============Try and except=========================================================

try:
    s = Student(name="Mouli",age=44)
except ValidationError as e:
    print("Error raised: ",e)
    
'''
Error raised:  1 validation error for Student
course
  Field required [type=missing, input_value={'name': 'Mouli', 'age': 44}, input_type=dict]    
'''
