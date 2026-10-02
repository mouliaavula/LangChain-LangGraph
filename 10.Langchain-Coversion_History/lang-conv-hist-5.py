import os
from langchain_openai import ChatOpenAI
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory

llm = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv("OPENAI_API_KEY"))

memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm = llm,
    memory=memory
)

result = conversation.invoke({
    "input":"My name Mouli."
})

"""
print("=================ConversationChain type==================================")
print(type(result))  # <class 'dict'>
print("\n=================History==================================")
print(result)
print("\n Input======================================")
print(result["input"])
print("\n History======================================")
print(result["history"])
print("\n Response======================================")
print(result["response"]) # observe key name is "response"
"""

result2 = conversation.invoke({
    "input":"I teach python."
})


print("=================ConversationChain type==================================")
print(type(result2))  # <class 'dict'>
print("\n=================History==================================")
print(result2)
print("\n Input======================================")
print(result2["input"])
print("\n History======================================")
print(result2["history"])
print("\n Response======================================")
print(result2["response"]) # observe key name is "response"