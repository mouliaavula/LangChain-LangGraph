import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Create Prompt
prompt = PromptTemplate.from_template(
    """
    Explain {topic} for a {level} learner.

    Requirements:
    - Use very simple English
    - Give a simple definition
    - Give 3 important points
    - Give one example
    """
)

# Create Model
model = ChatOpenAI(
    model="gpt-5.6-luna",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Create Parser
parser = StrOutputParser()

# Create Chain
chain = prompt | model | parser

print("1. invoke()")
print("2. batch()")
print("3. stream()")

choice = input("Enter your choice: ")

if choice == "1":
    result = chain.invoke(
            {
                "topic": "Python",
                "level": "Beginner"
            }
        )

    print("\nResult:")
    print(result)

elif choice == "2":

    inputs = [
        {
            "topic": "Python",
            "level": "Beginner"
        },
        {
            "topic": "Java",
            "level": "Beginner"
        },
        {
            "topic": "LangChain",
            "level": "Beginner"
        }
    ]

    results = chain.batch(inputs)

    for i, result in enumerate(
        results,
        start=1
    ):
        print(f"\n--- Result {i} ---")
        print(result)

elif choice == "3":

    print("\nStreaming Response:\n")

    for chunk in chain.stream(
        {
            "topic": "Generative AI",
            "level": "Beginner"
        }
    ):
        print(
            chunk,
            end="",
            flush=True
        )

    print()

else:

    print("Invalid choice")