import os 

from langchain_openai import ChatOpenAI
from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age:int
    course:str
llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv("OPENAI_API_KEY"))
str_llm = llm.with_structured_output(Student)

print("\n Normal LLM type:",type(llm))
#o/p: Normal LLM type: <class 'langchain_openai.chat_models.base.ChatOpenAI'>
print("\n Structured Output LLM Type:", type(str_llm))
#o/p: Structured Output LLM Type: <class 'langchain_core.runnables.base.RunnableSequence'>

normal_result = llm.invoke("Explain python in one line.")

str_result = str_llm.invoke("Ravi is 22 years old and learning python")

print("\n Normal Result type: ",type(normal_result))
#o/p: Normal Result type:  <class 'langchain_core.messages.ai.AIMessage'>
print("\n Structured output  Result type: ",type(str_result))
#o/p: Structured output  Result type:  <class '__main__.Student'>
print("\n Normal Result: ",normal_result)
print("\n Structured output Result: ",str_result)
