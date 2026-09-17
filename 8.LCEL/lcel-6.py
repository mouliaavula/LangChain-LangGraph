import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template(
    """
    Create a {days} days travel plan {place}
    Budget:{budget}
    Main interest : {interest}
    keep plan simple
    """
)

model = ChatOpenAI(model='gpt-5.6-luna',api_key=os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()

days = int(input("Enter number days:"))
place = input("Enter place:")
budget = int(input("Enter budget:"))
interest = input("main interest:")

chain = prompt | model | parser

res = chain.invoke({
    "days":days,
    "budget":budget,
    "interest": interest,
    "place":place
})

print(res)