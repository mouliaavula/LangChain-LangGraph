import os
from langchain_openai import ChatOpenAI

from langchain_core.messages import (HumanMessage, AIMessage)

llm = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    HumanMessage(content="My name is mouli"),
    AIMessage(content="Nice to meet you Mouli"),
    HumanMessage(content="What is my name")
]

response = llm.invoke(messages)
print(response.content)