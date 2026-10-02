import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template(
    """
    Explain {topic} in simple english.
    Give:
    Simple definition.
    3 important points
    one example
    """
)

model = ChatOpenAI(model='gpt-5.6-luna',api_key=os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()

chain = prompt | model | parser

result1 = chain.invoke({"topic":"Python"})
result2 = chain.invoke({"topic":"Java"})
result3 = chain.invoke({"topic":"SQL"})
result4 = chain.invoke({"topic":"Langchain"})

print("\n============================================================")
print(result1)
print("\n============================================================")
print(result2)
print("\n============================================================")
print(result3)
print("\n============================================================")
print(result4)