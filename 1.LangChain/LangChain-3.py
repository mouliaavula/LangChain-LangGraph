import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)
#llm = ChatOpenAI(model="gpt-4o",api_key=api_key)
system_message = SystemMessage(content="You are a experienced python trainer")
human_message = HumanMessage(content="Explain about python in a single line")
ai_message = llm.invoke([system_message,human_message])
print(type(ai_message))
print("\n")
print(ai_message)
print("\n")
print(ai_message.content)

