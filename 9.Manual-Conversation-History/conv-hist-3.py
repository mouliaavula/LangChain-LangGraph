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

question = HumanMessage(
    content="""
    What is my name?

    If my name is not available in the
    supplied conversation, say "I don't know".
    """
)


# WITHOUT HISTORY

response1 = llm.invoke(
    [question]
)

print("WITHOUT HISTORY")
print("----------------")
print(response1.content)


# WITH HISTORY

messages = [
    HumanMessage(
        content="My name is Durga."
    ),

    AIMessage(
        content="Nice to meet you."
    ),

    question
]

response2 = llm.invoke(
    messages
)

print("\nWITH HISTORY")
print("------------")
print(response2.content)