from langchain_core.chat_history import InMemoryChatMessageHistory

# Create Memory Object
history = InMemoryChatMessageHistory()

#Add Human message to history
history.add_user_message("My name Mouli")

# Add AI message to history
history.add_ai_message("Nice to meet you Mouli.")

print("=============Conversion History==================")
print("\n ============= type of history object: ",type(history))
print("\n ===========Total history object ")
print(history)
print("\n ============== Content from  history object ")
print(history)

# history.messages is a attribute inside InMemoryChatMessageHistory and that contains list of messages 
# i.e it's type is list
print("\n ==== messages type : ",type(history.messages))
print("\n ====================Messages inside history object")
for message in history.messages:
    print(type(message).__name__,":",message.content)
    
    
print("\n =================Explore on history Object ================ ")  
# dir : returns a list of names that you can access on the object.  
print(dir(history))
print("\n ========only public apis==============")
print([item for item in dir(history) if not item.startswith("_")])
print("\n ========dictionary view==============")
# __dict__ : Dictionary of instance attributes
print(history.__dict__)

"""
history
   ↓
┌──────────────────────────────────┐
│ InMemoryChatMessageHistory       │
│                                  │
│ messages → [ ... ]               │
│                                  │
│ methods → add_user_message()     │
│           add_ai_message()       │
│           clear()                │
└──────────────────────────────────┘
"""