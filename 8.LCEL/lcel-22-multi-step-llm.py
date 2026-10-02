import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

# -----------------------------------
# Step 1: Create Model
# -----------------------------------

model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

parser = StrOutputParser()

# -----------------------------------
# Step 2: Explanation Prompt
# -----------------------------------

explanation_prompt = PromptTemplate.from_template(
    """
    Explain {topic} to a beginner.

    Requirements:
    - Use very simple English
    - Give a simple definition
    - Give 5 important points
    - Give one example
    """
)

# -----------------------------------
# Step 3: Convert String to Dictionary
# -----------------------------------

prepare_quiz_input = RunnableLambda(
    lambda explanation: {
        "explanation": explanation
    }
)

# -----------------------------------
# Step 4: Quiz Prompt
# -----------------------------------

quiz_prompt = PromptTemplate.from_template(
    """
    Based only on the explanation below,
    generate 5 MCQs.

    For every MCQ provide:
    - Question
    - Four options
    - Correct answer

    Explanation:

    {explanation}
    """
)

# -----------------------------------
# Step 5: Create Sequential Chain
# -----------------------------------

chain = (
    explanation_prompt
    | model
    | parser
    | prepare_quiz_input
    | quiz_prompt
    | model
    | parser
)

# -----------------------------------
# Step 6: Read Input
# -----------------------------------

topic = input(
    "Enter topic: "
)

# -----------------------------------
# Step 7: Execute Complete Sequence
# -----------------------------------

result = chain.invoke(
    {
        "topic": topic
    }
)

# -----------------------------------
# Step 8: Display Result
# -----------------------------------

print("\n----------------------------")
print("FINAL QUIZ")
print("----------------------------")

print(result)

# batch 
inputs = [
    {"topic": "Python"},
    {"topic": "Java"},
    {"topic": "SQL"}
]

results = chain.batch(inputs)