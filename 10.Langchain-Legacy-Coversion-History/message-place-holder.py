from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# Create prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("history")
])


# Previous chat messages
history = [
    ("human", "My name is Durga."),
    ("ai", "Hello Durga!")
]


# Insert history into prompt
result = prompt.invoke({
    "history": history
})


# Print final messages
print(result.messages)

for message in result.messages:
    print(type(message).__name__, ":", message.content)