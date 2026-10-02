import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

first_message = HumanMessage(
    content="My name is Durga."
)

response1 = llm.invoke(
    [first_message]
)

print("FIRST RESPONSE")
print("--------------")
print(response1.content)

print("\nTYPE")
print("----")
print(type(response1))

messages = [
    first_message,

    # response1 is already an AIMessage
    response1,

    HumanMessage(
        content="What is my name?"
    )
]

response2 = llm.invoke(
    messages
)

print("\nSECOND RESPONSE")
print("---------------")
print(response2.content)