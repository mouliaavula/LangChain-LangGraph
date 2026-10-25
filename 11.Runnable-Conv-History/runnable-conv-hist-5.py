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
# CREATE PROMPT
# ========================================

prompt = ChatPromptTemplate.from_messages(

    [
        (
            "system",
            """
            You are a helpful AI assistant.
            Answer in simple English.
            """
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
# HISTORY-AWARE RUNNABLE
# ========================================

chatbot = RunnableWithMessageHistory(

    chain,

    get_session_history,

    input_messages_key="question",

    history_messages_key="history"
)


# ========================================
# SELECT SESSION
# ========================================

session_id = input(
    "Enter Session ID: "
)


print("\nAI Chatbot")
print("Type 'exit' to stop")
print("------------------------")


# ========================================
# CHAT LOOP
# ========================================

while True:

    user_input = input(
        "\nYou: "
    )


    if user_input.lower() == "exit":

        print("Chat ended.")

        break
    response = chatbot.invoke(

        {
            "question": user_input
        },

        config={
            "configurable": {
                "session_id": session_id
            }
        }
    )


    print(
        "AI:",
        response.content
    )