import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template(
    """
    Explain {topic} in simple english
    Give;
    -simple definition
    -3 important points
    -one example
    """
)

model = ChatOpenAI(model='gpt-4o',api_key=os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()

topic = input("Enter topic:")

chain = prompt | model | parser

result = chain.invoke({"topic":topic})
print(result)
