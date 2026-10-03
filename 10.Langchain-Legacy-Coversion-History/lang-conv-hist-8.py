import os 
from langchain_openai import ChatOpenAI
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain
from langchain_core.prompts import (
    ChatPromptTemplate, MessagesPlaceholder
)

llm = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv("OPENAI_API_KEY"))

memory = ConversationBufferMemory(
    memory_key='history',
    return_messages=True
)

prompt = ChatPromptTemplate.from_messages([
    ("system","""
     You are a Python teacher.
    Explain everything in very simple English.
    Assume the student is a beginner.
    Give simple examples wherever possible.
     """),
    MessagesPlaceholder(
        variable_name='history'
    ),
    
    ('human','{input}')
])

conversation =ConversationChain(
    llm = llm,
    memory = memory,
    prompt = prompt
)

print("\nLegacy AI chatbot")
print("\nEnter exit to stop")
print("\n")

while True:
    user_input = input("\nYou:")
    if user_input.lower()=="exit":
        print("\n Chatbot Ended")
        break
    result = conversation.invoke({
        "input":user_input
    })
    
    print("\n AI response")
    print(result['response'])