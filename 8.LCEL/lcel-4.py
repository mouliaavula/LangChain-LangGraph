import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template(
    """
    Explain {topic} in {language} at {level} level
    Give one simple example
    """
)

model = ChatOpenAI(model='gpt-4o',api_key=os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()

topic = input("Enter topic:")
language = input("Enter language:")
level = input("Enter level:")

chain = prompt | model | parser

res = chain.invoke({
    "topic":topic,
    "language":language,
    'level':level
})

print(res)
