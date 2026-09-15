import os 
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age:int
    course:str
    
llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv('OPENAI_API_KEY'))

str_llm = llm.with_structured_output(Student)
result = str_llm.invoke('Mouli is 44 years old and he is learning python')

print(type(result))
print(result)
print(result.name)
print(result.age)
print(result.course)
