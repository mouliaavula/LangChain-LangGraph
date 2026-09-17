import os
from langchain_openai import ChatOpenAI
# do below from cmd current virtual environment from vs code and make sure key should not be in quotes
# if you provide with any codes like "api_key_value", use #raw_key = os.getenv("OPENAI_API_KEY") 
# #OPENAI_API_KEY = raw_key.strip('"\'') if raw_key else None

# set OPENAI_API_KEY=
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)

question = input("Enter question:")
# llm.invoke() is used to send an input to an LLM and get its response.
# input type of llm.invoke() should be str or  list of messages or PromptValue or dict
response = llm.invoke(question)
# LLM response is a message of type AIMessage
# this message contains meta data as well along with actual response, so to get actual data use response.content
#<class 'langchain_core.messages.ai.AIMessage'>
print(type(response))
print(response.content)

# strip('"\'') : string may contain '' or "" like "Hello" or 'Hello', so "\' -->represents  " and '
# Remove ' and " from the outside of the string. within the string it can not be removed
