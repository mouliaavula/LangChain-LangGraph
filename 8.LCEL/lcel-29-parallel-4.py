import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel
)

model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

parser = StrOutputParser()

# Step 1
explanation_prompt = PromptTemplate.from_template(
    """
    Explain {topic} in very simple English.

    Give:
    - Definition
    - 5 key points
    - One example
    """
)

explanation_chain = (
    explanation_prompt
    | model
    | parser
)

# Convert string to dictionary
prepare_input = RunnableLambda(
    lambda text: {
        "content": text
    }
)

# Parallel Branch 1
summary_prompt = PromptTemplate.from_template(
    """
    Summarize the following content
    in 3 short lines:

    {content}
    """
)

summary_chain = (
    summary_prompt
    | model
    | parser
)

# Parallel Branch 2
quiz_prompt = PromptTemplate.from_template(
    """
    Generate 5 beginner MCQs
    from the following content:

    {content}
    """
)

quiz_chain = (
    quiz_prompt
    | model
    | parser
)

# Parallel Branch 3
social_prompt = PromptTemplate.from_template(
    """
    Create a short social-media post
    from the following content:

    {content}
    """
)

social_chain = (
    social_prompt
    | model
    | parser
)

parallel = RunnableParallel(
    summary=summary_chain,
    quiz=quiz_chain,
    social_post=social_chain
)

final_chain = (
    explanation_chain
    | prepare_input
    | parallel
)

result = final_chain.invoke(
    {
        "topic": "Machine Learning"
    }
)

print("\nSUMMARY")
print(result["summary"])

print("\nQUIZ")
print(result["quiz"])

print("\nSOCIAL POST")
print(result["social_post"])