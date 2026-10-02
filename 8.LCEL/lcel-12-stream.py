import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time

prompt = PromptTemplate.from_template(
    '''
    Explain {topic} in simple english
    in about 5 points
    '''
)

model = ChatOpenAI(model='gpt-5.6-luna',api_key=os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()

chain = prompt | model | parser

s = chain.stream({"topic":"Langchain"})

print(type(s))

for chunk in s:
    #print(type(chunk)) # TextAccessor
    print(chunk)
'''    
for chunk in s:
    print(chunk)
    time.sleep(3)
'''