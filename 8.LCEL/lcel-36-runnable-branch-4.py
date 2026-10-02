import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda,RunnableBranch


model = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()

# Beginner prompt

beginner_prompt = PromptTemplate.from_template(
    '''
    Create BEGINNER study material
    on {topic}.

    Use very simple English.

    Include:
    1. Simple definition
    2. Five important points
    3. One simple example
    '''
)

# -------------------------
# Intermediate Prompt
# -------------------------

intermediate_prompt = PromptTemplate.from_template(
    """
    Create INTERMEDIATE study material
    on {topic}.

    Include:
    1. Definition
    2. Detailed explanation
    3. Important concepts
    4. Practical example
    5. Common mistakes
    """
)

# -------------------------
# Advanced Prompt
# -------------------------

advanced_prompt = PromptTemplate.from_template(
    """
    Create ADVANCED study material
    on {topic}.

    Include:
    1. Internal concepts
    2. Architecture
    3. Advanced explanation
    4. Practical implementation
    5. Best practices
    6. Interview questions
    """
)


beginner_chain = beginner_prompt  | model | parser
intermediate_chain = intermediate_prompt  | model | parser
advanced_chain = advanced_prompt  | model | parser


branch_runnable = RunnableBranch(
    (lambda x: x['level'].lower()=='beginner',beginner_chain),
    (lambda x: x['level'].lower()=='intermediate',intermediate_chain),
    advanced_chain
)
topic = input("Enter topic:")
level = input("Enter level:")
res = branch_runnable.invoke({"topic":topic,"level":level})
print(res)