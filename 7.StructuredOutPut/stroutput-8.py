import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class Student(BaseModel):
    name:str=Field(description='Name of the student')
    age:int | None = Field(default=None, description='Age of the student')
    technology:str | None = Field(default=None, description='Technology of the student')
    experience:int | None = Field(default=None, description='Experience of the student')

llm = ChatOpenAI(model='gpt-5.6-luna',api_key=os.getenv("OPENAI_API_KEY"))
str_llm = llm.with_structured_output(Student,include_raw=True)

text = input("Enter student information: ")
prompt = f""" Extract Student Information.
Rules:
1.Use only the supplied text
2.Do not invent information
3.if optional information is unavailable use null
Text:{text}
"""

res = str_llm.invoke(prompt)
if res["parsing_error"] is None:
    s = res['parsed']
    print("\n parsing is successful")
    print("\n Name:",s.name)
    print("\n Age:",s.age)
    print("\n Technology:",s.technology)
    print("\n Experience:",s.experience)
else:
    print("\n Parsing Failed")
    print(res['parsing_error'])
    print("\n Raw model response:",res['raw'])

