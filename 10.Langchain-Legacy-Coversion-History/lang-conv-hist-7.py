import os

from langchain_openai import ChatOpenAI
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory


# ========================================
# CREATE MODEL
# ========================================


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)


# ========================================
# CREATE LEGACY MEMORY
# ========================================

memory = ConversationBufferMemory()


# ========================================
# CREATE LEGACY CONVERSATION CHAIN
# ========================================

conversation = ConversationChain(
    llm=llm,
    memory=memory
)


print("Legacy AI Chatbot")
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


    result = conversation.invoke(
        {
            "input": user_input
        }
    )


    print(
        "AI:",
        result["response"]
    )