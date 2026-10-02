from langchain_classic.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    return_messages=True
)

memory.save_context(
    {"input":"I am Mouli."},
    {"output":"Nice to meet you, Moui."}
)

memory.save_context(
    {"input":"I teach python."},
    {"output":"Tha's great."}
)

print("\n Before clear memory==========================")
print(memory.load_memory_variables({}))

print("\n After clear memory==========================")
memory.clear()
print(memory.load_memory_variables({}))

