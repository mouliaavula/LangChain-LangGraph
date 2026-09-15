import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Literal

class SupportTicket(BaseModel):
    category:Literal[
        'billing','technical','account','other'
        ] = Field(description ='Main Category of the Customer Issue')
    priority:Literal[
        'Low','Medium','High'
    ] = Field(description ='Priority level of the issue')
    severity:int = Field(ge=1,le=5,description='Severity from 1 to 5')
    summary:str = Field(description='Short summary of the customer issue')
    
llm = ChatOpenAI(model='gpt-5.6-luna',api_key=os.getenv('OPENAI_API_KEY'))
str_llm = llm.with_structured_output(SupportTicket)
text = input("Enter customer issue")
res = str_llm.invoke(text)
print("\n Support ticket")
print("\n Category:",res.category)
print("\n Priority:",res.priority)
print("\n Severity:",res.severity)
print("\n Summary:",res.summary)


# My payment was deducted twice from my credit card.Please refund the extra amount.
# I forgot my password and cannot login to my account.