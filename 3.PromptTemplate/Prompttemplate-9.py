import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Create model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Create reusable template
template = PromptTemplate.from_template(
    """
    Teach me {topic}.

    Student Level: {level}
    Language: {language}
    Explanation Style: {style}

    Requirements:
    1. Explain in easy language.
    2. Give 5 important points.
    3. Give 2 real-life examples.
    4. Mention one common mistake.
    5. End with a one-line conclusion.
    """
)

# Take user inputs
topic = input("Enter topic: ")
level = input("Enter your level: ")
language = input("Enter language: ")
style = input("Enter explanation style: ")

# Generate prompt
prompt = template.invoke(
    {
        "topic": topic,
        "level": level,
        "language": language,
        "style": style
    }
)

# Inspect generated prompt
print("\n========== GENERATED PROMPT ==========")
print(prompt.to_string())

# Send to model
response = llm.invoke(prompt)

# Display response
print("\n========== AI RESPONSE ==========")
print(response.content)