import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful python trainer'),
        ('human','Explain {topic}')
    ]
)

print(chat_template.input_variables)
#o/p:['topic']
chat_prompt = chat_template.invoke({
    "topic":"Decorators"
})

llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv("OPENAI_API_KEY"))
response = llm.invoke(chat_prompt)
print(response.content)