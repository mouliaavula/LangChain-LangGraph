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

prompt1 = PromptTemplate.from_template(
    """
    Explain {topic} in very simple English.

    Give a simple definition and
    5 important points.
    """
)

to_dict = RunnableLambda(
    lambda explanation: {
        "explanation": explanation
    }
)

prompt2 = PromptTemplate.from_template(
    """
    Based on the explanation below,
    create 5 beginner interview questions.

    Explanation:

    {explanation}
    """
)

chain = (
    prompt1
    | model
    | parser
    | to_dict # by commenting this also it works because langchain takes care of compatibility conversion
    | prompt2
    | model
    | parser
)

result = chain.invoke(
    {
        "topic": "Python"
    }
)

print(result)