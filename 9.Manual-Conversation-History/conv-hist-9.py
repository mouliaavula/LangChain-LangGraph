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
        "\nYou: "
    )

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    messages.append(
        HumanMessage(
            content=user_input
        )
    )

    response = llm.invoke(
        messages
    )

    print(
        "AI:",
        response.content
    )

    messages.append(
        response
    )


    # --------------------------------
    # PRINT CURRENT HISTORY
    # --------------------------------

print("\nCurrent History:")
print("----------------")

for message in messages:
	print(type(message).__name__,":",message.content)