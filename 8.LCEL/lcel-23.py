#How to get intermediate values from the chain:

import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers  import StrOutputParser
from langchain_core.runnables import RunnableLambda
values = {}
def add_ten(x):
    result = x + 10
    values["after_add"] = result
    return result

def multiply_two(x):
    result = x  * 2
    values['after_multiply'] = result
    return result

def subtract_five(x):
    result = x - 5
    values['after_subtract']= result
    return result

add = RunnableLambda(add_ten)    
multiply = RunnableLambda(multiply_two)
subtract = RunnableLambda(subtract_five)

chain = add | multiply | subtract

result = chain.invoke(5)

print("\result :",result)
print("\n Intermediate values:")

print("\n value after add :", values['after_add'])
print("\n value after multiply :", values['after_multiply'])
print("\n value after subtract :", values['after_subtract'])