import os

from typing import Literal

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class SentimentResult(BaseModel):

    sentiment: Literal[
        "positive",
        "negative",
        "neutral"
    ] = Field(
        description="Overall sentiment of the text"
    )

    confidence: float = Field(
        ge=0,
        le=1,
        description="Confidence score between 0 and 1"
    )

    reason: str = Field(
        description="Very short reason for the sentiment"
    )

llm = ChatOpenAI(
    model="gpt-5.6-luna",
    api_key=os.getenv("OPENAI_API_KEY")
)

structured_llm = llm.with_structured_output(
    SentimentResult
)

text = input(
    "Enter customer feedback: "
)

result = structured_llm.invoke(text)

print("\nSENTIMENT ANALYSIS")
print("------------------")

print("Sentiment  :", result.sentiment)
print("Confidence :", result.confidence)
print("Reason     :", result.reason)