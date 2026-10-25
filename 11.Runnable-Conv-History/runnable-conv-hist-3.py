import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

# Create Model
llm = ChatOpenAI(
    model='gpt-4o-mini',api_key=os.getenv("OPENAI_API_KEY")
)

# create store
store = {}

# get session history

def get_session_history(session_id):
    if session_id not in store:
        store[session_id]=(InMemoryChatMessageHistory())
    return store[session_id]

# Wrap model with runnable chat message history
chatbot = RunnableWithMessageHistory(
    llm, get_session_history
)

# Messages about mouli
#1
response = chatbot.invoke(
    [HumanMessage(content="My name is mouli")],
    config={
        "configurable":{
            "session_id":"mouli"
        }
    }
)

# print(response.content)
#2: 
chatbot.invoke(
    [HumanMessage(content="I teach Langchain")],
    config={
        "configurable":{
            "session_id":"mouli"
        }
    }
)

#3:
chatbot.invoke(
    [HumanMessage(content="I live in Hyderabad")],
    config={
        "configurable":{
            "session_id":"mouli"
        }
    }
)


# Messages about Neethu
#1
response = chatbot.invoke(
    [HumanMessage(content="My name is neethu")],
    config={
        "configurable":{
            "session_id":"neethu"
        }
    }
)

# print(response.content)
#2: 
chatbot.invoke(
    [HumanMessage(content="I got school")],
    config={
        "configurable":{
            "session_id":"neethu"
        }
    }
)

#3:
chatbot.invoke(
    [HumanMessage(content="I like mathematics")],
    config={
        "configurable":{
            "session_id":"neethu"
        }
    }
)


# question by user base

response = chatbot.invoke(
    [HumanMessage(content="what do you know about me")],
    config={
        "configurable":{
            "session_id":"neethu" # mouli --> gives mouli info and neethu--> gives neethu info
        }
    }
)

print(response.content)




