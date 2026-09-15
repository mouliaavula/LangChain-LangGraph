import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class Employee(BaseModel):
    name:str= Field(description='Name of the employee')
    technology:str = Field(description='Primary technology of the employee')
    experience:int = Field(description='Professional Experience in years')
    
llm = ChatOpenAI(model='gpt-5.6-luna',api_key=os.getenv("OPENAI_API_KEY"))
str_llm = llm.with_structured_output(Employee,include_raw=True)
result = str_llm.invoke("Ravi is java developer with 6 years of experience")

print("\n Result type:", type(result))
print("\n Result: ",result)
print("\n Raw message:", result["raw"])
print("\n Parsed message:", result["parsed"])
print("\n Parsing Error:", result["parsing_error"])