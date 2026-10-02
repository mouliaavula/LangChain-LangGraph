import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)


messages = []


while True:
   user_input = input(
        "You: "
    )

   # Stop chatbot
   if user_input.lower() == "exit":
       print("Chat ended.")
       break

    # Add user message
   messages.append(
       HumanMessage(
            content=user_input
        )
    )

    # Send complete history
   response = llm.invoke(
        messages
    )
 # Display AI response
   print(
        "AI:",
        response.content
    )

    # Add AI response
   messages.append(
        response
    )
   print(
        "\nNumber of messages:",
        len(messages)
    )