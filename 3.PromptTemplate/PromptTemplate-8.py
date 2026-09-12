import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv("OPENAI_API_KEY"))

prompt_temple = PromptTemplate.from_template("Explain {topic} in {language} in {style}")

topic = input("Enter topic: ")
language = input("Enter language: ")
style = input("Enter style: ")
prompt = prompt_temple.invoke({
    "topic":topic,
    "language":language,
    "style":style
})

response = llm.invoke(prompt)
print(response.content)