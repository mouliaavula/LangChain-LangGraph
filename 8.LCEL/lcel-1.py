# Manual approach to call/invoke all components

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template("Explain {topic} in simple English")

model = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()

prompt_value = prompt.invoke({"topic":"Java"})

response = model.invoke(prompt_value)

result = parser.invoke(response)
print(result)