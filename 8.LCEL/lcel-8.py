import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Step 1: Create Prompt Template
prompt = PromptTemplate.from_template(
    """
    Explain {topic} to a {level} learner.

    Requirements:
    - Use very simple English
    - Give a simple definition
    - Give 5 important points
    - Give one real-world example
    - Give one-line conclusion
    """
)

# Step 2: Create Chat Model
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Step 3: Create Output Parser
parser = StrOutputParser()

# Step 4: Create LCEL Chain
chain = prompt | model | parser

# Step 5: Read User Input
topic = input("Enter topic: ")
level = input("Enter learner level: ")

# Step 6: Execute Chain
result = chain.invoke(
    {
        "topic": topic,
        "level": level
    }
)

# Step 7: Display Result
print("\n-----------------------------")
print("FINAL RESPONSE")
print("-----------------------------")
print(result)