import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)

# ai_message = llm.invoke() here if we pass message variables then in invoke it should be list [] object
# but if we pass string then we can pass as "Hello my is mouli" something like overloading

ai_message = llm.invoke("Hello my name is Mouli")
print(ai_message.content)

ai_message = llm.invoke("WOW Excellent, what is my name")
print(ai_message.content)

# Model can not remember anything once response sent. ie. Model can not remember previous conversation history
