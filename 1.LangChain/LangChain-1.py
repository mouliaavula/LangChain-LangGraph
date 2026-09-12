import os
from langchain_openai import ChatOpenAI


# do below from cmd current virtual environment from vs code and make sure key should not be in quotes
# if you provide with any codes like "api_key_value", use #raw_key = os.getenv("OPENAI_API_KEY") 
# #OPENAI_API_KEY = raw_key.strip('"\'') if raw_key else None

# set OPENAI_API_KEY=
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)

question = input("Enter question:")
response = llm.invoke(question)
print(response.content)

