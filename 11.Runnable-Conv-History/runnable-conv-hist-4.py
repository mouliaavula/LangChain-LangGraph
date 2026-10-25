import os

from langchain_openai import ChatOpenAI

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain_core.chat_history import (
    InMemoryChatMessageHistory
)

from langchain_core.runnables.history import (
    RunnableWithMessageHistory
)


# ========================================
# CREATE MODEL
# ========================================

llm = ChatOpenAI(
    model="gpt-5.6-luna",
    api_key=os.getenv("OPENAI_API_KEY")
)


# ========================================
# CREATE CHAT PROMPT
# ========================================

prompt = ChatPromptTemplate.from_messages(
  [
        (
            "system",
            "You are a helpful AI assistant."
        ),

        MessagesPlaceholder(
            variable_name="history"
        ),

        (
            "human",
            "{question}"
        )
    ]
)

# ========================================
# CREATE LCEL CHAIN
# ========================================
chain = (
    prompt
    | llm
)


# ========================================
# SESSION HISTORY STORE
# ========================================

store = {}


def get_session_history(session_id):

    if session_id not in store:

        store[session_id] = (
            InMemoryChatMessageHistory()
        )
    return store[session_id]


# ========================================
# WRAP LCEL CHAIN WITH HISTORY
# ========================================

chatbot = RunnableWithMessageHistory(

    chain,

    get_session_history,

    input_messages_key="question",

    history_messages_key="history"
)



# ========================================
# FIRST MESSAGE
# ========================================

response1 = chatbot.invoke(

    {
        "question":
        "My name is Durga."
    },

    config={
        "configurable": {
            "session_id": "session1"
        }
    }
)



print(
    "AI:",
    response1.content
)


# ========================================
# SECOND MESSAGE
# ========================================

response2 = chatbot.invoke(

    {
        "question":
        "What is my name?"
    },

    config={
        "configurable": {
            "session_id": "session1"
        }
    }
)


print(
    "AI:",
    response2.content
)