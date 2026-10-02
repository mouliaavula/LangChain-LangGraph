import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


# ========================================
# CREATE CHAT MODEL
# ========================================

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

# ========================================
# STEP 1 — FIRST USER MESSAGE
# ========================================

first_message = HumanMessage(
    content="My name is Durga."
)

response1 = llm.invoke(
    [first_message]
)

print("FIRST RESPONSE")
print("--------------")
print(response1.content)


# ========================================
# STEP 2 — NEW CALL WITHOUT HISTORY
# ========================================

question = HumanMessage(
    content="""
    What is my name?

    If my name is not available in the
    supplied conversation,
    say "I don't know".
    """
)

response2 = llm.invoke(
    [question]
)

print("\nWITHOUT HISTORY")
print("----------------")
print(response2.content)


# ========================================
# STEP 3 — SAME QUESTION WITH HISTORY
# ========================================

messages = [
    first_message,
    response1,
    question
]

response3 = llm.invoke(
    messages
)

print("\nWITH HISTORY")
print("------------")
print(response3.content)