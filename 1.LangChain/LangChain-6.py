import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)

human_message = HumanMessage(content="Hello My name is Mouli")

ai_message = llm.invoke(human_message)
print(ai_message.content)


# ValueError: Invalid input type must be promptvalue , str, ot list

