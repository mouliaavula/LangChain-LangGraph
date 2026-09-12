# stroutputparser : it wll convert model output into plain text/string 

import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv("OPENAI_API_KEY"))
response = llm.invoke("Explain python in one line")
str_parser = StrOutputParser()
output_parser = str_parser.invoke(response)
print(type(output_parser))
#o/p:<class 'langchain_core.messages.base.TextAccessor'>
print(output_parser)
print()
print()
print(type(response.content))
#o/p:<class 'str'>
print(response.content)