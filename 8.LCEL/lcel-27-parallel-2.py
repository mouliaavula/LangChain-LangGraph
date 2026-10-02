import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (RunnableSequence,RunnableLambda,RunnableParallel)

model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

parser = StrOutputParser()

joke_prompt = PromptTemplate.from_template(
    "Tell one clean short joke about {topic}."
)

motivation_prompt = PromptTemplate.from_template(
    """
    Give one short motivational message
    related to {topic}.
    """
)

joke_chain = (
    joke_prompt
    | model
    | parser
)

motivation_chain = (
    motivation_prompt
    | model
    | parser
)

parallel_chain = RunnableParallel(
    joke = joke_chain,
    motivation = motivation_chain
)

res = parallel_chain.invoke({"topic":"Programming"})
print(res)
print(res['joke'])
print(res['motivation'])