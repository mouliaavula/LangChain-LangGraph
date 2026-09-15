import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class Student(BaseModel):
    name:str = Field(description='Name of the student')
    age:int | None = Field(default=None, description='Age of student if available')
    course:str | None = Field(default=None,description='Name of the course')
    email:str | None = Field(default=None,description='Email of the student')

llm = ChatOpenAI(model='gpt-5.6-luna',api_key=os.getenv('OPENAI_API_KEY'))
str_llm = llm.with_structured_output(Student)
text = input("Enter text:")
prompt = f"""
Extract student information.

Rules:
- Use only the supplied information.
- Do not invent missing values.
- Use null for optional information that is unavailable.

Student Information:
{text}
"""
student = str_llm.invoke(prompt)

print("\nSTUDENT INFORMATION")
print("-------------------")

print("Name   :", student.name)
print("Age    :", student.age)
print("Course :", student.course)
print("Email  :", student.email)
