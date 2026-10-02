from langchain_core.runnables import (RunnableLambda,RunnableBranch)

pass_runnable = RunnableLambda(
    lambda marks : "Pass"
)

fail_runnable = RunnableLambda(
    lambda marks : "Fail"
)

branch_runnable =RunnableBranch(
    (lambda marks : marks>=35,pass_runnable),
    fail_runnable
)

print(branch_runnable.invoke(50))
print(branch_runnable.invoke(20))