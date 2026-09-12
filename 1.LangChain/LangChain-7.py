import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)

human_message1 = HumanMessage(content="Hello My name is Mouli")

ai_message1 = llm.invoke([human_message1])
print(ai_message1.content)

human_message2 = HumanMessage(content="What is my name")

ai_message2 = llm.invoke([human_message1, ai_message1,human_message2])
print(ai_message2.content)


