import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

template = PromptTemplate.from_template(
    """
    Explain {topic} to a beginner.

  
  Use:
    - Very simple English
    - 5 important points
    - One real-life example
    """
)

topic = input("Enter topic: ")

prompt = template.invoke(
    {
        "topic": topic
    }
)

response = llm.invoke(prompt)
print(response.content)