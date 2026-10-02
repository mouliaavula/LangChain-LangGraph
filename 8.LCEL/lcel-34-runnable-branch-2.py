from langchain_core.runnables import (RunnableLambda,RunnableBranch)

distinction = RunnableLambda(
    lambda x: "Distinction"
)

first_class = RunnableLambda(
    lambda x: "First Class"
)

passed = RunnableLambda(
    lambda x: "Passed"
)

fail = RunnableLambda(
    lambda x: "fail"
)


branch_runnable = RunnableBranch(
    (lambda x : x >=90 ,distinction),
    (lambda x : x >=60 , first_class),
    (lambda x : x >=35 , passed),
    fail
)

print(branch_runnable.invoke(95))
print(branch_runnable.invoke(70))
print(branch_runnable.invoke(50))
print(branch_runnable.invoke(30))