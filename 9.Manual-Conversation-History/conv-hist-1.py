import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv("OPENAI_API_KEY"))

response1 = llm.invoke("My name is mouli")
print("\n First response")
print(response1.content)
print("\n")

response2 = llm.invoke('''
What is my name.
if my name is not available in the supplied conversation say I don not know.
''')

print("\n Second response")
print(response2.content)
print("\n")


