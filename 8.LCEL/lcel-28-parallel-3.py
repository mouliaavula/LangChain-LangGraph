import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

parser = StrOutputParser()

blog_prompt = PromptTemplate.from_template(
    """
    Write a short beginner-friendly blog
    about {topic}.

    Requirements:
    - Simple title
    - Simple introduction
    - 5 important points
    - One-line conclusion
    """
)

social_prompt = PromptTemplate.from_template(
    """
    Create a short social-media post
    about {topic}.

    Keep it simple and engaging.
    """
)

summary_prompt = PromptTemplate.from_template(
    """
    Summarize {topic} in 3 short lines
    for a beginner.
    """
)

blog_chain = (
    blog_prompt
    | model
    | parser
)

social_chain = (
    social_prompt
    | model
    | parser
)

summary_chain = (
    summary_prompt
    | model
    | parser
)

parallel_chain = RunnableParallel(
    blog=blog_chain,
    social_post=social_chain,
    summary=summary_chain
)

topic = input("Enter topic: ")

result = parallel_chain.invoke(
    {
        "topic": topic
    }
)

print("\n==============================")
print("BLOG")
print("==============================")
print(result["blog"])

print("\n==============================")
print("SOCIAL POST")
print("==============================")
print(result["social_post"])

print("\n==============================")
print("SUMMARY")
print("==============================")
print(result["summary"])