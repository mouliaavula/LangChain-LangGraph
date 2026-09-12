import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful python trainer'),
        ('human','Explain loops'),
        ('ai','Loops is important concept in python'),
        ('human','Explain conditional statements in python')
    ]
)

chat_prompt = chat_template.invoke({})

llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv("OPENAI_API_KEY"))
response = llm.invoke(chat_prompt)
print(response.content)