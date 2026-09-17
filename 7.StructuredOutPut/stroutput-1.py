import os 
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age:int
    course:str
    
llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv('OPENAI_API_KEY'))

# llm.with_structured_output(Student) --> This does create another Python object, 
# but it is better to think of it as a configured runnable/wrapper around the LLM ,
# according to the Student structure, rather than a second completely separate OpenAI model instance.

str_llm = llm.with_structured_output(Student)
result = str_llm.invoke('Mouli is 44 years old and he is learning python')

print(type(result))
#o/p:<class '__main__.Student'>
print(result)
print(result.name)
print(result.age)
print(result.course)

# llm and str_llm are different objects but  str_llm is just wrapper on llm according to given structure 
# str_llm = llm + structure
print()
print(type(llm))
#o/p:<class 'langchain_openai.chat_models.base.ChatOpenAI'>
print(type(str_llm))
#o/p:<class 'langchain_core.runnables.base.RunnableSequence'>
print(llm is str_llm)
#o/p:False
print(id(llm))
print(id(str_llm))
