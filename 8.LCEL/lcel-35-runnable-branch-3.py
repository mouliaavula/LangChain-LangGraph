from langchain_core.runnables import RunnableLambda, RunnableBranch


pass_runnable= RunnableLambda(
    lambda x : f'{x['name']} passed the exam'
)

fail_runnable = RunnableLambda(
    lambda x : f'{x['name']} fail the exam'
)

runnable_branch = RunnableBranch(
    (lambda x : x['marks'] > 35,pass_runnable),
    fail_runnable
)

result = runnable_branch.invoke({"marks":50,"name":"Nithwik"})
print(result)