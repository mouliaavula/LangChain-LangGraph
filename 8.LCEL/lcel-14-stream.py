import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template(
    """
    Create a {days}-day travel plan for {place}.

    Budget: {budget}
    Main Interest: {interest}

    Keep the answer simple.
    """
)

model = ChatOpenAI(
    model="gpt-5.6-luna",
    api_key=os.getenv("OPENAI_API_KEY")
)

parser = StrOutputParser()

chain = prompt | model | parser

print("1. invoke")
print("2. batch")
print("3. stream")

choice = input("Enter choice: ")

if choice == "1":

    result = chain.invoke(
        {
            "days": 3,
            "place": "Goa",
            "budget": "Medium",
            "interest": "Beaches"
        }
    )

    print(result)

elif choice == "2":

    inputs = [
        {
            "days": 3,
            "place": "Goa",
            "budget": "Medium",
            "interest": "Beaches"
        },
        {
            "days": 2,
            "place": "Hyderabad",
            "budget": "Low",
            "interest": "Food"
        }
    ]

    results = chain.batch(inputs)

    for result in results:
        print("\n--------------------")
        print(result)

elif choice == "3":

    for chunk in chain.stream(
        {
            "days": 3,
            "place": "Goa",
            "budget": "Medium",
            "interest": "Beaches"
        }
    ):
        print(chunk, end="", flush=True)

    print()

else:

    print("Invalid choice")