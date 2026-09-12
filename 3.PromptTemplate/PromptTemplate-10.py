lsimport os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

template = PromptTemplate.from_template(
    """
    Create a simple travel plan for {place}.

    Duration: {days} days
    Budget: {budget}

    Include:
    - Places to visit
    - Suggested daily plan
    - Food suggestions
    - Simple travel tips
    """
)

place = input("Enter destination: ")
days = input("Enter number of days: ")
budget = input("Enter budget type (low/medium/high): ")

prompt = template.invoke(
    {
        "place": place,
        "days": days,
        "budget": budget
    }
)

response = llm.invoke(prompt)

print("\nTravel Plan:")
print(response.content)
