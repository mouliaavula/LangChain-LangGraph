import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template(
    """
    Generate {count} {level} interview questions
    about {technology}
    --Use simple english
    """
)

model = ChatOpenAI(model='gpt-4o',api_key=os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()

count = input("Enter of number Questions:")
level = input("Enter level:")
technology = input("Enter technology:")

chain = prompt | model | parser

res = chain.invoke({
    "count":count,
    "level":level,
    "technology":technology
})

print(res)