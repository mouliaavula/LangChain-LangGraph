import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda


add_ten = RunnableLambda(
    lambda x : x + 10
)

multiply_two = RunnableLambda(
    lambda x : x * 2
)

subtract_five = RunnableLambda(
    lambda x : x - 5
)

chain = (add_ten | multiply_two | subtract_five)
#chain = add_ten | multiply_two | subtract_five

result = chain.invoke(5)

print(type(result))
print(result)


print(chain.steps)
print(chain.first)
print(chain.last)
print(chain.middle)

