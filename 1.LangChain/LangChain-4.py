import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)
#llm = ChatOpenAI(model="gpt-4o",api_key=api_key)
system_message = SystemMessage(content="You are a experienced python trainer")
human_message = HumanMessage(content="Explain about python in a single line")
ai_message = llm.invoke([system_message,human_message])
print("\n")
print(ai_message.content)

system_message = SystemMessage(content="You are a experienced Life skills Coach")
human_message = HumanMessage(content="Explain about LAW of Attraction")
ai_message = llm.invoke([system_message,human_message])
print("\n")
print(ai_message.content)

