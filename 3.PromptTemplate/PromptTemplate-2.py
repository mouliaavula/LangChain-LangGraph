import os
from langchain_core.prompts import PromptTemplate
prompt_template = PromptTemplate.from_template("Explain {topic} in simple english")
topic = input("Enter Input:")
result = prompt_template.invoke(
    {
        "topic":topic #now it is completely dynamic
    }
)
print(type(result))
print(result)
print(result.text)
print(result.to_string())
