import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)


# Empty conversation history
messages = []


# User message
user_input = "My name is Durga."


# Add user message to history
messages.append(
    HumanMessage(
        content=user_input
    )
)


# Send complete history to model
response = llm.invoke(
    messages
)


print("AI:", response.content)


# Add AI response to history
messages.append(
    response
)


print("\nConversation History:")
print(messages)