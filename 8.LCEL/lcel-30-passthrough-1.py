from langchain_core.runnables import(
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough)

double = RunnableLambda(lambda x :  2 * x)

parallel = RunnableParallel(
    original = RunnablePassthrough(),
    double = double
)

res = parallel.invoke(10)
print(res)
print("original : ",res['original'])
print("double of input : ",res['double'])

