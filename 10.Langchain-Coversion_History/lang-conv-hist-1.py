from langchain_classic.memory import ConversationBufferMemory

# Create memory object

memory = ConversationBufferMemory()

# save conversion history manually to legacy memory

memory.save_context(
    {"input":"I am Mouli."},
    {"output":"Nice to meet you, Mouli."}
)

# read stored memory

result = memory.load_memory_variables({})

print(result) # formatted string 

print(result["history"])

