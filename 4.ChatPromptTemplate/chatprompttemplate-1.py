# PromptTemplate is used to create dynamic reusable text based prompts
# ChatPromptTemplate is used to create dynamic reusable message based prompts

import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage('You are a helpful python trainer'),
        HumanMessage("Explain loops in python"),
        AIMessage("Loops are important concept in python"),
        HumanMessage("Explain conditional statements in python")
    ]
)

#print(type(chat_template))
# <class 'langchain_core.prompts.chat.ChatPromptTemplate'>
#print(chat_template)
""" 
o/p:
    input_variables=[] input_types={} partial_variables={} messages=[SystemMessage(content='You are a helpful python trainer', 
    additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain loops in python', additional_kwargs={},
    response_metadata={}), AIMessage(content='Loops are important concept in python', additional_kwargs={},
    response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
    HumanMessage(content='Explain conditional statements in python', additional_kwargs={}, response_metadata={})]
"""

chat_prompt = chat_template.invoke({})
print(type(chat_prompt))
#<class 'langchain_core.prompt_values.ChatPromptValue'>
print()
print(chat_prompt)
print()
print(chat_prompt.messages)

for message in chat_prompt.messages:
    print(type(message).__name__,":",message.content)
    
llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv("OPENAI_API_KEY"))
response = llm.invoke(chat_prompt)
print(response.content)