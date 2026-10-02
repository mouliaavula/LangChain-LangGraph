
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableParallel

add_ten = RunnableLambda(lambda x : x + 10)
double = RunnableLambda(lambda x : x * 2)
square = RunnableLambda(lambda x : x * x)

parallel = RunnableParallel(add = add_ten,double=double,square=square)

res = parallel.invoke(5)
print(type(res))
print(res)
print(res['add'])
print(res['double'])
print(res['square'])

'''
o/p:
<class 'dict'>
{'add': 15, 'double': 10, 'square': 25}
15
10
25

'''