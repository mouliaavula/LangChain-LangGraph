#How to get intermediate values from the chain:
import os
from langchain_core.runnables import RunnableLambda
values = {}
def save(name,value):
    values[name]=value
    return value
add_ten = RunnableLambda(
    lambda x : save("after_add",x+10)
)

multiply_two = RunnableLambda(
    lambda x : save("after_multiply",x * 2)
)

subtract_five = RunnableLambda(
    lambda x : save("after_subtract",x - 5)
)

chain = add_ten | multiply_two | subtract_five

res = chain.invoke(5)
print(res)
print(values)