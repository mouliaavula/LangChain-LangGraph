import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# C--> Create components
prompt = PromptTemplate.from_template("Explain {topic} in simple english")

model = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()
#prompt, model , parser are called components

# C--> create chain
chain = prompt | model | parser

# Execute chain
result = chain.invoke({"topic":"python"})
# here we are passing input first component if it needed, here we have
# topic is needed prompt component we have to pass it
print(result)

# CCE -->
#C---->Create components
#C--->Create chain
#E--->Execute chain