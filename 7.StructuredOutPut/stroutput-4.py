import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class Product(BaseModel):
    name:str = Field(description='Name os the product')
    category:str = Field(description='Category of the product')
    price:float = Field(description='Price of the product')
    
llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv('OPENAI_API_KEY'))
str_llm = llm.with_structured_output(Product)
text = input("Enter product information:")
res = str_llm.invoke(text)
print(res)
print(res.model_dump())
print(res.model_dump_json())