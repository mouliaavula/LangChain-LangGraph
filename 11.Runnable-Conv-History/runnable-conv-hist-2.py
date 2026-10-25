import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Create model
llm = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv("OPENAI_API_KEY"))

# store
store = {}

# Get Session history

def get_session_history(session_id):
    if session_id  not in store:
        store[session_id] = (InMemoryChatMessageHistory())
    return store[session_id]

# Wrap the model with Runnable chat message history
chatbot = RunnableWithMessageHistory(
    llm,
    get_session_history
)

# First Message
response = chatbot.invoke(
    [HumanMessage(content="My name mouli")],
    config={
        "configurable":{
            "session_id":"mouli"
        }
    }
)
#print(response.content)    

#Second message
response = chatbot.invoke(
    [HumanMessage(content="what is my name")],
    config={
        "configurable":{
            "session_id":"mouli"
        }
    }
)
# print(response.content)

# Third message

response = chatbot.invoke(
    [HumanMessage(content="What is my name")],
    config={
        "configurable":{
            "session_id":"manu"
        }
    }
)
print(response.content)

"""
I'm sorry, but I don't have access to personal information about individuals unless 
it has been shared in the course of our conversation. If you'd 
like to share your name or any other information, feel free to let me know! 
reason: we passed session id as "manu" but and with that session id we did not share any info about ravi
but if we pass session id as "mouli" , we get info about mouli
"""