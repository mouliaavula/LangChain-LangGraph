from langchain_classic.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    return_messages=True # to return messages instead formatted string
)

memory.save_context(
    {"input":"I am Mouli."},
    {"output":"Nice to meet you, Mouli."}
)

memory.save_context(
    {"input":"I teach python"},
    {"output":"That's great."}
)

result = memory.load_memory_variables({})

print("\n=============================================")
print(result)
print("\n=============================================")
print(result["history"])
print("\n=============================================")
for message in result["history"]:
    print(type(message).__name__,":",message.content)