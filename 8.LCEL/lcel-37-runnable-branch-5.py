import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch


model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

parser = StrOutputParser()


luxury_prompt = PromptTemplate.from_template(
    """
    Create a LUXURY travel plan.

    Destination: {destination}
    Days: {days}
    Budget: {budget}

    Include:
    - Luxury hotel
    - Premium transportation
    - Best tourist places
    - Fine dining
    - Day-wise plan
    """
)


standard_prompt = PromptTemplate.from_template(
    """
    Create a STANDARD travel plan.

    Destination: {destination}
    Days: {days}
    Budget: {budget}

    Include:
    - Good hotel
    - Transportation
    - Important tourist places
    - Food suggestions
    - Day-wise plan
    """
)


budget_prompt = PromptTemplate.from_template(
    """
    Create a BUDGET travel plan.

    Destination: {destination}
    Days: {days}
    Budget: {budget}

    Include:
    - Budget accommodation
    - Low-cost transportation
    - Important tourist places
    - Affordable food
    - Day-wise plan
    """
)


luxury_chain = (
    luxury_prompt
    | model
    | parser
)

standard_chain = (
    standard_prompt
    | model
    | parser
)

budget_chain = (
    budget_prompt
    | model
    | parser
)


travel_agent = RunnableBranch(

    (
        lambda x: x["budget"] >= 100000,
        luxury_chain
    ),

    (
        lambda x: x["budget"] >= 50000,
        standard_chain
    ),

    budget_chain
)


result = travel_agent.invoke(
    {
        "destination": "Goa",
        "days": 5,
        "budget": 75000
    }
)

print(result)