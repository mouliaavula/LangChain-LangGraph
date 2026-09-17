import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template(
    """
    Give a simple recipe for {dish}.

    Requirements:
    - Ingredients
    - Step-by-step preparation
    - Simple English
    """
)

model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

parser = StrOutputParser()

chain = prompt | model | parser

dish = input("Enter dish: ")

result = chain.invoke(
    {
        "dish": dish
    }
)

print(result)