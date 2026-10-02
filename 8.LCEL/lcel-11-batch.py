import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template(
    """
    Explain {topic} in simple english.
    Give:
    Simple Definition.
    3 important points
    one example
    """
)

model = ChatOpenAI(model='gpt-5.6-luna',api_key= os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()

input = [
    {"topic":"Python"},
    {"topic":"Java"},
    {"topic":"Sql"},
    {"topic":"Langchain"}
]

chain = prompt | model | parser

results = chain.batch(input)
# input type is list of dic
print(type(results)) # List
print("\n =================With batch()=========================")
for result in results:
    print(result)
    print("\n ==========================================")
    
    
# or we can use zip() function
print("\n*********************************with zip() function*****************************************")
for technology, result in zip(["Python","Java","Sql"],results):
    print("\n-------------------------------------------------------------------")
    print(technology)   
    print("\n-------------------------------------------------------------------")
    print(result)
    
    
# The below also valid i.e alternate to batch() but it is sequential execution where as in batch it is parallel processing 
print("\n +++++++++++++++++++++++++++++++Alternate to batch()+++++++++++++++++++++++++++++++++++++++++")
for topic in input:
    print(chain.invoke(topic))
    print("\n ======================================================")