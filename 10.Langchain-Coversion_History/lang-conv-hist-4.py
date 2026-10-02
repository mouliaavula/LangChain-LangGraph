from langchain_classic.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=2)

memory.save_context(
    {"input":"I am Mouli."},
    {"output":"Nice to meet you, Moui."}
)

memory.save_context(
    {"input":"I teach python."},
    {"output":"Tha's great."}
)

memory.save_context(
    {"input":"I live in Hyderabad"},
    {"output":"Okay."}
)

print(memory.load_memory_variables({}))