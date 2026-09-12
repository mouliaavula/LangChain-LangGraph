import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# To create prompt template
template = PromptTemplate.from_template("Explain {topic} at {level} level")

# To see what are input variables are there in prompt template
# print(template.input_variables)
# o/p:['level', 'topic']


#template.invoke() is used to fill input variables and return formatted prompt
formatted_prompt = template.invoke({
    "topic":"Python",
    "level":"Beginner"
})

# To get/see formatted prompt. 
#print(formatted_prompt.to_string())
# o/p:Explain Python at Beginner level

llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv("OPENAI_API_KEY"))
response = llm.invoke(formatted_prompt)
print(response.content)