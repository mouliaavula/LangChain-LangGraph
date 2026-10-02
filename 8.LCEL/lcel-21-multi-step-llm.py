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

outline_prompt = PromptTemplate.from_template(
    """
    Create a short blog outline about {topic}.

    Give 5 headings.
    """
)

prepare_blog_input = RunnableLambda(
    lambda outline: {
        "outline": outline
    }
)

blog_prompt = PromptTemplate.from_template(
    """
    Write a beginner-friendly blog
    using this outline:

    {outline}

    Use simple English.
    """
)

chain = (
    outline_prompt
    | model
    | parser
    | prepare_blog_input
    | blog_prompt
    | model
    | parser
)

result = chain.invoke(
    {
        "topic": "Benefits of Artificial Intelligence"
    }
)

print(result)
