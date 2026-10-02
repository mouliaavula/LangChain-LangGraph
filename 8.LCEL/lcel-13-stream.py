import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time

prompt = PromptTemplate.from_template(
    """
    Explain {topic} in very simple English.

    Give:
    - Definition
    - 5 important points
    - One example
    - One-line conclusion
    """
)

model = ChatOpenAI(model='gpt-5.6-luna',api_key=os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()

chain = prompt | model | parser

for chunk in chain.stream({"topic":"quantum ai"}):
    print(chunk, end="",flush=True)
