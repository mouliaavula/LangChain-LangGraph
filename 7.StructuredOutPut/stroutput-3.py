import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class Employee(BaseModel):
    name:str = Field(description='Name of the employee')
    technology:str = Field(description='Primary technology of the employee')
    exp:int = Field(description='Experience of the employee')
    
llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv('OPENAI_API_KEY'))
str_llm = llm.with_structured_output(Employee)
text = input("Enter employee information:")
res = str_llm.invoke(text)
print(res)