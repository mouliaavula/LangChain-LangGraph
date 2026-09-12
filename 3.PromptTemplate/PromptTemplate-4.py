import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv("OPENAI_API_KEY"))

prompt_template = PromptTemplate.from_template("Give me a simple recipe for {dish}. Explain step by step")

dish = input("Enter dish name:")
prompt = prompt_template.invoke(
    {
        "dish":dish
    }
)
response = llm.invoke(prompt)
print(response.content)
