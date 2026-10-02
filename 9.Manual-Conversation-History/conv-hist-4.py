import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

messages = [
    HumanMessage(
        content="My favorite technology is Python."
    ),

    AIMessage(
        content="Great choice."
    ),

    HumanMessage(
        content="What is my favorite technology?"
    )
]

response = llm.invoke(messages)

print(response.content)