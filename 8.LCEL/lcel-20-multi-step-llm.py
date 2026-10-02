import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

parser = StrOutputParser()

explanation_prompt = PromptTemplate.from_template(
    """
    Explain {topic} for a beginner.

    Use very simple English.
    Give one real-world example.
    """
)

prepare_quiz_input = RunnableLambda(
    lambda explanation: {
        "content": explanation
    }
)

quiz_prompt = PromptTemplate.from_template(
    """
    Based only on the following content,
    generate 5 MCQs.

    Content:

    {content}
    """
)

chain = (
    explanation_prompt
    | model
    | parser
    | prepare_quiz_input
    | quiz_prompt
    | model
    | parser
)

result = chain.invoke(
    {"topic": "Machine Learning"}
)

print(result)