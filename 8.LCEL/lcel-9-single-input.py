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

result = chain.invoke({"topic":"Python"})

print(result)