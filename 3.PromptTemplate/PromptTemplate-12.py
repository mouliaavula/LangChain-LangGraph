import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

template = PromptTemplate.from_template(
    """
    Suggest 10 restaurant names.

    Cuisine: {cuisine}
    Style: {style}
    Location: {location}

    Names should be:
    - Easy to remember
    - Attractive
    - Suitable for the restaurant
    """
)

cuisine = input("Enter cuisine: ")
style = input("Enter restaurant style: ")
location = input("Enter location: ")

prompt = template.invoke(
    {
        "cuisine": cuisine,
        "style": style,
        "location": location
    }
)

response = llm.invoke(prompt)

print("\nRestaurant Name Ideas:")
print(response.content)