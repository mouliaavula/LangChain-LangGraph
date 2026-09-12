import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

template = PromptTemplate.from_template(
    """
    Generate {count} interview questions on {technology}
    for a {level} candidate.

    For every question:
    - Give the question
    - Give a simple answer
    """
)

technology = input("Enter technology: ")
level = input("Enter level: ")
count = input("How many questions?: ")

prompt = template.invoke(
    {
        "technology": technology,
        "level": level,
        "count": count
    }
)

response = llm.invoke(prompt)
print("\n AI Response")
print(response.content)