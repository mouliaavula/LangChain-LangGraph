# Master project
import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableLambda,RunnableSequence,RunnableParallel,RunnablePassthrough
)

# model
model = ChatOpenAI(model='gpt-5.6-luna',api_key=os.getenv('OPENAI_API_KEY'))
# Parser
parser = StrOutputParser()

# Ste 1 core explanation

explanation_prompt = PromptTemplate.from_template(
    '''
    Explain {topic} for {audience}
    Requirements:
    Use simple english
    Give clear definition
    Give 5 key points
    Give one real world example
    '''
)

explanation_chain = explanation_prompt | model | parser 

# Convert String to dictionary

prepare_parallel_input = RunnableLambda(
    lambda explanation : {"content":explanation}
)

# Summary branch

summary_prompt = PromptTemplate.from_template(
    '''
    Summary the following content in 5 bullet points
    {content}
    '''
)

summary_chain = summary_prompt | model | parser

# Quiz branch 

quiz_prompt = PromptTemplate.from_template(
    """
    Generate 5 beginner MCQs
    based only on this content:

    {content}

    Give four options and the correct answer.
    """
)

quiz_chain = quiz_prompt | model | parser

# Social post

social_prompt = PromptTemplate.from_template(
    """
    Create a short social-media post
    from the following content:

    {content}

    Keep it simple and engaging.
    """
)

social_chain = social_prompt | model | parser

# Interview Questions branch

interview_prompt = PromptTemplate.from_template(
    """
    Generate 5 beginner interview questions
    from the following content:

    {content}
    """
)


interview_chain = interview_prompt | model | parser


parallel_stage = RunnableParallel(
    summary = summary_chain,
    quiz = quiz_chain,
    social  = social_chain,
    interview =interview_chain
)
final_chain = explanation_prompt | model | prepare_parallel_input | parallel_stage

topic = input("Enter topic:")
audience = input("Enter audience:")
result = final_chain.invoke({
    "topic":topic,
    "audience": audience
})

# ----------------------------------
# DISPLAY
# ----------------------------------

print("\n================================")
print("SUMMARY")
print("================================")
print(result["summary"])

print("\n================================")
print("QUIZ")
print("================================")
print(result["quiz"])

print("\n================================")
print("SOCIAL POST")
print("================================")
print(result["social"])

print("\n================================")
print("INTERVIEW QUESTIONS")
print("================================")
print(result["interview"])