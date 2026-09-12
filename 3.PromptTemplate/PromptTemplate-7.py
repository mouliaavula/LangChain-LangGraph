import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm  = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv("OPENAI_API_KEY"))

prompt_template = PromptTemplate.from_template("Explain {topic} in  {language} in {style}")

#print(prompt_template.input_variables)
#o/p: ['language', 'style', 'topic']

prompt = prompt_template.invoke({
    "topic":"Python",
    "language":"Telugu",
    "style":"simple"
})
# print(prompt.to_string())
# o/p: Explain Python in  Telugu in simple
response = llm.invoke(prompt)
print(response.content)
