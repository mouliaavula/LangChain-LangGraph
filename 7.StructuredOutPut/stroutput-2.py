import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class Student(BaseModel):
    name:str = Field(description='Name of student')
    age:int = Field(description='Age of student')
    course:str = Field(description='Name of the course')
llm = ChatOpenAI(model='gpt-5.6',api_key=os.getenv('OPENAI_API_KEY'))

str_llm = llm.with_structured_output(Student)
text = input("Enter student information:")
res = str_llm.invoke(text)

print(res)