import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt_template = PromptTemplate.from_template("Explain {topic} in one line")

topic = input("Enter topic: ")
prompt = prompt_template.invoke({
    "topic":topic
})

llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv("OPENAI_API_KEY"))

response = llm.invoke(prompt)

str_parser = StrOutputParser()
str_output = str_parser.invoke(response)
print(str_output)