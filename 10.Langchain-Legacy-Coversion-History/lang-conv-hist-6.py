import os 
from langchain_openai import ChatOpenAI
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferWindowMemory

llm = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv("OPENAI_API_KEY"))

memory = ConversationBufferWindowMemory(k=2)

conversation = ConversationChain(
    llm= llm,
    memory=memory
)

conversation.invoke({
    "input":"My name is Mouli"
})

conversation.invoke({
    "input":"I teach python"
})

result = conversation.invoke({
    "input":"I will live in Hyderabad"
})
print("\n complete dictionary============================")
print(result)

print("\n Window history============================")
print(memory.load_memory_variables({}))
