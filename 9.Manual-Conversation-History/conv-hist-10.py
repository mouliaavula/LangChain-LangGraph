import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)


# Complete conversation history
messages = []


# Maximum recent messages sent to model
MAX_MESSAGES = 6


while True:

    user_input = input(
        "\nYou: "
    )


    if user_input.lower() == "exit":

        print("Chat ended.")

        break
  # Add user message to complete history
    messages.append(
        HumanMessage(
            content=user_input
        )
    )


    # Select recent conversation
    recent_messages = messages[
        -MAX_MESSAGES:
    ]


    # Send only recent history
    response = llm.invoke(
        recent_messages
    )


    print(
        "AI:",
        response.content
    )


    # Store AI response in complete history
    messages.append(
        response
    )